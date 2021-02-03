import os
import shutil
from glob import glob
import subprocess

def _copy_package():
    # Copy Tangent USD Build to rez build dir

    src = os.environ["REZ_BUILD_SOURCE_PATH"]
    dst = os.environ["REZ_BUILD_INSTALL_PATH"] + "/build"

    # Remove existing build
    if os.path.exists(dst):
        print(" - Removing existing build")
        shutil.rmtree(dst)

    dirs = [
        ".",
    ]

    for d in dirs:
        try:
            shutil.copytree(src + "/" + d, dst + "/" + d, ignore=shutil.ignore_patterns('_rez_build', '.git', 'otls'))
            print(" - Copying: {0} : {1}".format(src + "/" + d, dst + "/" + d))
        except Exception as e:
            print(" - " + str(e))
            pass

    remove_files = [
        dst + '/package.py',
        dst + '/rez_build.py',
    ]

    for f in remove_files:
        print(" - Removing:" + str(f))
        if os.path.exists(f):
            os.remove(f)
            print("   - Done")

def _compile_otls():

    print(" - Compiling OTLs")

    # Get all root level folder hdas
    source_dir = '{package_dir}/otls/*/'.format(package_dir=os.environ["REZ_BUILD_SOURCE_PATH"])
    release_dir = '{package_dir}/build/otls/'.format(package_dir=os.environ["REZ_BUILD_INSTALL_PATH"])
    os.mkdir(release_dir)

    dirs = glob(source_dir)

    # Loop through all expanded hda's
    for p in dirs:
        source_hda_path = os.path.normpath(p)

        if source_hda_path.endswith('backup'):
            continue

        print(" - Compiling: " + os.path.basename(source_hda_path))

        # Build path of new compiled hda
        compiled_name = "compiled_" + os.path.basename(source_hda_path)
        compiled_hda_path = os.path.join(os.path.dirname(release_dir), compiled_name)

        # Remove existing compiled hda
        if os.path.exists(compiled_hda_path):
            os.remove(compiled_hda_path)

        # Compile
        sub = subprocess.call([
            'hotl',
            '-l',
            source_hda_path,
            compiled_hda_path
        ])



if __name__ == "__main__":

    print("=== Build Package ===")
    
    _copy_package()
    _compile_otls()

    print("=== Complete! ===")
