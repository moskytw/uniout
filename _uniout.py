#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['Uniout', 'unescape']

import sys
import re

escape_x_re = re.compile(r'(?:\\x[0-9a-f]{2})+')
escape_u_re = re.compile(r'(?:\\u[0-9a-f]{4}|\\U[0-9a-f]{8})+')
encoding = sys.getfilesystemencoding()

def unescape(s):
    r'''decode the \x, \u and \U in a escaped string -> encoded string'''

    s = escape_x_re.sub(lambda m: m.group().decode('string-escape'), s)
    s = escape_u_re.sub(lambda m: m.group().decode('unicode-escape').encode(encoding), s)

    # for Python < 2.7
    if isinstance(s, unicode):
        s = s.encode(encoding)

    return s

def runs_in_ipython():
    '''Check if we are in IPython.'''
    import __builtin__
    return '__IPYTHON__' in __builtin__.__dict__ and \
           __builtin__.__dict__['__IPYTHON__']

class Uniout(object):
    '''It simulates a stream object, but unescapes the escaped bytes before
    writing.'''

    def __init__(self, stream):

        self.stream = stream

        # make uniout look like the stream
        for attr_name in dir(stream):
            if not attr_name.startswith('_'):
                setattr(self, attr_name, getattr(stream, attr_name))

        # modify the write method to de-escape
        self.write = lambda bytes: self.stream.write(unescape(bytes))
