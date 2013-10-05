from distutils.core import setup

from uniout import __version__

setup(
    name = 'uniout',
    description = 'Never see escaped bytes in output.',
    long_description = open('README.rst').read(),
    version = __version__,
    author = 'Mosky',
    author_email = 'mosky.tw@gmail.com',
    #url = 'http://uniout.mosky.tw/',
    url = 'https://github.com/moskytw/uniout',
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

