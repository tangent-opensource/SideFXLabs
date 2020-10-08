name = 'sidefxlabs'

version = '1.218-ta.1.1.0'

authors = [
    'benjamin.skinner',
    'sidefx',
]

build_requires = [
    'python-3',
]

requires = [
    'houdini',
]

variants = [
    ['houdini-18.0'],
]

build_command = "python {root}/rez_build.py"

def commands():

    # Split and store version and package version
    split_versions = str(version).split('-')
    env.SIDEFXLABS_VERSION.set(split_versions[0])
    env.SIDEFXLABS_PACKAGE_VERSION.set(split_versions[1])

    env.sidefxlabs_current_version.set("MANUAL")
    env.SIDEFXLABS.set( '{root}\\build' )
    
    env.PATH.prepend( '{0}\\bin'.format(env.SIDEFXLABS) )
    env.HOUDINI_PATH.append( '{0};&'.format(env.SIDEFXLABS) )
