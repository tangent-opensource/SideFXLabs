name = 'sidefxlabs'

version = '1.218+ta.1.0.0'

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
    env.sidefxlabs_current_version.set("MANUAL")
    env.SIDEFXLABS.set( '{root}\\build' )
    
    env.PATH.prepend( '{0}\\bin'.format(env.SIDEFXLABS) )
    env.HOUDINI_PATH.append( '{0};&'.format(env.SIDEFXLABS) )
