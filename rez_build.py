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
            shutil.copytree(src + "/" + d, dst + "/" + d, ignore=shutil.ignore_patterns('_rez_build', '.git'))
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

if __name__ == "__main__":

    print("=== Build Package ===")
    
    _copy_package()

    print("=== Complete! ===")
