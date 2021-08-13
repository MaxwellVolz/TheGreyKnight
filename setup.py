from distutils.core import setup
import py2exe


py2exe_options = {
                    'ascii':True,
                    'excludes':['_ssl',
                        'pyreadline', 'difflib', 'doctest', 'locale', 
                        'optparse', 'pickle', 'calendar'
                        'pdb','inspect', 'unittest'
                        ],
                    'dll_excludes':['msvcr71.dll'],  # Exclude msvcr71
                    'compressed':True,
                    "includes": ["imp"]
                    }
                    


setup(name='TheGreyKnight',
        version='0.1.0',
        description='Hardcore Roguelike TextAdventure',
        author='Maxwell Volz',
        console=['main.py'],
        options={'py2exe': py2exe_options},
        )