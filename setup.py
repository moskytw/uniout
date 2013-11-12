#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import _uniout

setup(

    name = 'uniout',
    version = _uniout.__version__,
    description = 'Never see escaped bytes in output.',
    long_description = open('README.rst').read(),

    author = 'Mosky',
    url = 'https://github.com/moskytw/uniout',
    author_email = 'mosky.tw@gmail.com',
    license = 'MIT',
    platforms = 'any',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    py_modules = ['_uniout', 'uniout'],

)

