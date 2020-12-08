name = 'sidefxlabs'

version = '18.0.665-ta.1.0.0'

authors = [
    'benjamin.skinner',
    'sidefx',
]

build_requires = [
    'python-2',
]

requires = [
    'houdini',
]

variants = [
    # Technically we probably should be tying these to the labs version,
    # however, we might need new labs updates/features that are compatible
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
