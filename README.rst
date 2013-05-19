Uniout
======

Print the object representation in readable unicode char instead of the code of
char.

Usage
-----

Just import this module.

::

    import uniout

Example
-------

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
