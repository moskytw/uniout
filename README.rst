.. .. image:: https://img.shields.io/pypi/v/uniout.svg
..    :target: https://pypi.python.org/pypi/uniout
..
.. .. image:: https://img.shields.io/pypi/dm/uniout.svg
..    :target: https://pypi.python.org/pypi/uniout

Uniout
======

It makes Python print the object representation in readable chars instead of the
escaped string.

Example
-------

>>> from pprint import pprint
>>> langs = [
...     'Hello, world!',
...     '你好，世界！',
...     'こんにちは世界',
...     u'Hello, world!',
...     u'你好，世界！',
...     u'こんにちは世界'
... ]
... 

Before:

>>> pprint(langs)
['Hello, world!',
 '\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81',
 '\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xe4\xb8\x96\xe7\x95\x8c',
 u'Hello, world!',
 u'\u4f60\u597d\uff0c\u4e16\u754c\uff01',
 u'\u3053\u3093\u306b\u3061\u306f\u4e16\u754c']

After:

>>> import uniout
>>> pprint(langs)
['Hello, world!',
 '你好，世界！',
 'こんにちは世界',
 u'Hello, world!',
 u'你好，世界！',
 u'こんにちは世界']

Installation
------------

You can install it via PyPI,

::

    sudo pip install uniout

or download it manually.

Changelog
---------

v0.3.7
~~~~~~

1. Switch to long-string syntax (``'''`` or ``"""``) automatically.

v0.3.6
~~~~~~

1. Fixed the issue with empty string.

v0.3.5
~~~~~~

1. Make it still works for files.

v0.3.4
~~~~~~

1. A better fix for the previous bug.

v0.3.3
~~~~~~

1. Fixed the problem that Uniout can't be installed by PIP.

v0.3.2
~~~~~~

1. Show the original string if the escaped string can't be decoded properly.
2. Use better way to find string literals.
3. Print more correct unescaped string representation.

v0.3.1
~~~~~~

1. Fixed a bug when Uniout works with IPython.

v0.3
~~~~

Thanks for the pull requests `#3 <https://github.com/moskytw/uniout/pull/3>`_ and `#4 <https://github.com/moskytw/uniout/pull/4>`_ from `@timtan <https://github.com/timtan>`_, it now

1. works well with `IPython <http://ipython.org/>`_,
2. and also supports stderr.
