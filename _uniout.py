import re
import sys
# the helpers

escape_x_re = re.compile(r'(?:\\x[0-9a-f]{2})+')
escape_u_re = re.compile(r'(?:\\u[0-9a-f]{4}|\\U[0-9a-f]{8})+')
encoding = sys.getfilesystemencoding()

def dexuescape(s):
    r'''decode the \x, \u and \U in a escaped string -> encoded string'''
    s = escape_x_re.sub(lambda m: m.group().decode('string-escape'), s)
    s = escape_u_re.sub(lambda m: m.group().decode('unicode-escape').encode(encoding), s)

    # for Python < 2.7
    if isinstance(s, unicode):
        s = s.encode(encoding)

    return s

# make uniout
uniout = lambda: 'middleware of stdout' # any instance

# make uniout look like stdout
for attrname in dir(sys.stdout):
    if not attrname.startswith('__'):
        setattr(uniout, attrname, getattr(sys.stdout, attrname))

# modify the write method to de-escape
uniout.write = lambda s: sys.__stdout__.write(dexuescape(s))

__all__ = ['uniout', 'dexuescape' ]
