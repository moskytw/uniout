Uniout
======

It makes Python print the object representation in readable chars instead of the
escaped string.

Usage
-----

Just import this module.

::

    import uniout

An Example
----------

::

    # test.py
    data = ['中文', 'にほんご', u'Λλ']
    print 'Before:', data
    import uniout
    print 'After :', data

Result of test.py:

::

    Before: ['\xe4\xb8\xad\xe6\x96\x87', '\xe3\x81\xab\xe3\x81\xbb\xe3\x82\x93\xe3\x81\x94', u'\u039b\u03bb']
    After : ['中文', 'にほんご', u'Λλ']

Installation
------------

You can install it via PyPI,

::

    sudo pip install uniout

or download it manually.
