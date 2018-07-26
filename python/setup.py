from distutils.core import setup, Extension


module1 = Extension('c',
                    define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '0')],
#                    include_dirs = ['/usr/local/include'],
#                    libraries = [''],
#                    library_dirs = ['/usr/local/lib'],
                    sources = ['cmodule.c'])


setup (name = 'C Module',
       version = '1.0',
       description = 'Description of C Module',
       author = 'Tyler Cromwell',
       author_email = 'tjc6185@gmail.com',
       url = 'https://github.com/tyler-cromwell/Examples',
       long_description = '''Long description of C Module''',
       ext_modules = [module1])

