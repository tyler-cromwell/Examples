from distutils.core import setup, Extension

major = '1'
minor = '0'
debug = '0'
full = '\"{}.{}.{}\"'.format(major, minor, debug)

module1 = Extension('c',
                    define_macros = [('MAJOR_VERSION', major),
                                     ('MINOR_VERSION', minor),
                                     ('DEBUG_VERSION', debug),
                                     ('FULL_VERSION', full)],
#                    include_dirs = ['/usr/local/include'],
#                    libraries = [''],
#                    library_dirs = ['/usr/local/lib'],
                    sources = ['cmodule.c'])


setup (name = 'C Module',
       version = full,
       description = 'Description of C Module',
       author = 'Tyler Cromwell',
       author_email = 'tjc6185@gmail.com',
       url = 'https://github.com/tyler-cromwell/Examples',
       long_description = '''Long description of C Module''',
       ext_modules = [module1])

