#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['unescape', 'make_unistream', 'runs_in_ipython']

import sys
import re

try:
    import chardet
except ImportError:
    chardet = None

string_literal_re = re.compile(r'''(?<![uU])(?P<q>['"]).+?(?<!\\)(?P=q)''')
unicode_literal_re = re.compile(r'''[uU](?P<q>['"]).+?(?<!\\)(?P=q)''')

def unescape_string_literal(b, target_encoding):

    b = b.decode('string-escape')

    if chardet:

        r = chardet.detect(b)
        confidence, b_encoding = r['confidence'], r['encoding']

        if confidence >= 0.5 and b_encoding != target_encoding:
            try:
                b = b.decode(b_encoding)
            except (UnicodeDecodeError, LookupError):
                pass
            else:
                b = b.encode(target_encoding)

    b = b[0]+b[1:-1].replace(b[0], '\\'+b[0])+b[-1]

    return b

def unescape_unicode_literal(b, target_encoding):
    b = b.decode('unicode-escape')
    b = b[:2]+b[2:-1].replace(b[1], '\\'+b[1])+b[-1]
    return b.encode(target_encoding)

def unescape(b, target_encoding=None):

    if target_encoding is None:
        target_encoding = sys.stdout.encoding

    b = string_literal_re.sub(lambda m: unescape_string_literal(m.group(), target_encoding), b)

    b = unicode_literal_re.sub(lambda m: unescape_unicode_literal(m.group(), target_encoding), b)

    return b

def make_unistream(stream):

    unistream = lambda: 'middleware'

    # make unistream look like the stream
    for attr_name in dir(stream):
        if not attr_name.startswith('_'):
            setattr(unistream, attr_name, getattr(stream, attr_name))

    # modify the write method to de-escape
    unistream.write = lambda bytes: stream.write(unescape(bytes, unistream.encoding))

    return unistream

def runs_in_ipython():
    '''Check if we are in IPython.'''
    import __builtin__
    return '__IPYTHON__' in __builtin__.__dict__ and \
           __builtin__.__dict__['__IPYTHON__']
