from distutils.core import setup

from uniout import __version__

setup(
    name    = 'uniout',
    description = 'It makes Python print the object representation in readable chars instead of the escaped string.',
    long_description = open('README.rst').read(),
    version = __version__,
    author  = 'Mosky',
    author_email = 'mosky.tw@gmail.com',
    #url = 'http://uniout.mosky.tw/',
    py_modules = ['uniout'],
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

