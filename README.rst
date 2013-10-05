Uniout
======

It makes Python print the object representation in readable chars instead of the
escaped string.

Example
-------

Here we have a Python script, test.py:

::

    # test.py

    data = ['中文', 'にほんご', u'Λλ']
    print 'Before:', data

    import uniout
    print 'After :', data

The output of test.py:

::

    Before: ['\xe4\xb8\xad\xe6\x96\x87', '\xe3\x81\xab\xe3\x81\xbb\xe3\x82\x93\xe3\x81\x94', u'\u039b\u03bb']
    After : ['中文', 'にほんご', u'Λλ']

Installation
------------

You can install it via PyPI,

::

    sudo pip install uniout

or download it manually.

Change Log
----------

v0.3
~~~~

Thanks for the pull requests `#3 <https://github.com/moskytw/uniout/pull/3>`_ and `#4 <https://github.com/moskytw/uniout/pull/4>`_ from `@timtan <https://github.com/timtan>`_, it now

1. works well with IPython,
2. and also supports stderr.
