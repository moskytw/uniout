#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import re
import sys

# the helpers

escape_x_re = re.compile(r'(?:\\x..)+')
escape_u_re = re.compile(r'(?:\\u....|\\U........)+')
encoding = sys.getfilesystemencoding()

def dexuescape(s):
    r'''decode the \x, \u and \U in a escaped string -> encoded string'''
    s = escape_x_re.sub( lambda m: m.group().decode('string-escape'), s)
    s = escape_u_re.sub( lambda m: m.group().decode('unicode-escape').encode(encoding), s)
    return s

# make uniout

uniout = lambda: 'middleware of stdout' # any instance

# make uniout to look like stdout
for attrname in dir(sys.stdout):
    if not attrname.startswith('__'):
        setattr( uniout, attrname, getattr(sys.stdout, attrname) )

# modify the write method to de-escape
uniout.write = lambda s: sys.__stdout__.write( dexuescape(s) )

if __name__ != '__main__':
    # install the uniout
    sys.stdout = uniout

    # just insert `import uniout` in your script to take effect

else:
    import unittest

    class TestUniout(unittest.TestCase):

        def test_deescape_x(self):
            i = r'\xe4\xb8\xad\xe6\x96\x87'
            o = r'中文'
            self.assertEqual( dexuescape(i), o)

        def test_deescape_x_with_n(self):
            i = r'\xe4\xb8\xad\n\xe6\x96\x87'
            o = r'中\n文'
            self.assertEqual( dexuescape(i), o)

        def test_deescape_u(self):
            i = r"\u4e2d\u6587"
            o = r'中文'
            self.assertEqual( dexuescape(i), o)

        def test_deescape_u_with_n(self):
            i = r"\u4e2d\n\u6587"
            o = r'中\n文'
            self.assertEqual( dexuescape(i), o)

        def test_mixed(self):
            i = r"\xe4\xb8\xad\n\xe6\x96\x87\u4e2d\n\u6587"
            o = r'中\n文中\n文'
            self.assertEqual( dexuescape(i), o)

    unittest.main()
