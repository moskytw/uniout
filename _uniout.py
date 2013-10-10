#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def literalize(content, is_unicode=False):
    '''Literalize the content.

    Examples:

    >>> print literalize('str')
    'str'
    >>> print literalize('\'str\'')
    "'str'"
    >>> print literalize('\"\'str\'\"')
    '"\'str\'"'
    '''

    quote_mark = "'"
    if "'" in content:
        quote_mark = '"'
        if '"' in content:
            quote_mark = "'"
            content = content.replace(r"'", r"\'")

    return 'u'[not is_unicode:]+quote_mark+content+quote_mark

string_literal_re = re.compile(r'''(?<![uU])(?P<q>['"]).+?(?<!\\)(?P=q)''')
unicode_literal_re = re.compile(r'''[uU](?P<q>['"]).+?(?<!\\)(?P=q)''')

def unescape_string_literal(b, target_encoding):
    '''Unescape string literal.

    Examples:

    >>> print unescape_string_literal(r"'\xe4\xb8\x96\xe7\x95\x8c\xe4\xbd\xa0\xe5\xa5\xbd'", 'utf-8')
    '世界你好'

    >>> print unescape_string_literal(r"'\xa5@\xac\xc9\xa7a\xa6n'", 'utf-8')
    '\xa5@\xac\xc9\xa7a\xa6n'
    '''

    b = b[1:-1].decode('string-escape')

    try:
        b.decode(target_encoding)
    except UnicodeDecodeError:
        b = b.encode('string-escape')

    return literalize(b)

def unescape_unicode_literal(b, target_encoding):
    '''Unescape unicode literal.

    Examples:

    >>> print unescape_unicode_literal(r"u'\u4e16\u754c\u4f60\u597d'", 'utf-8')
    u'世界你好'
    '''

    return literalize(
        b[2:-1].decode('unicode-escape').encode(target_encoding),
        is_unicode=True
    )

def unescape(b, target_encoding):
    '''Unescape all string and unicode literals.'''

    b = string_literal_re.sub(lambda m: unescape_string_literal(m.group(), target_encoding), b)
    b = unicode_literal_re.sub(lambda m: unescape_unicode_literal(m.group(), target_encoding), b)
    return b

def make_unistream(stream):
    '''Make a stream which unescapes literals before to write.'''

    unistream = lambda: 'middleware'

    # make unistream look like the stream
    for attr_name in dir(stream):
        if not attr_name.startswith('_'):
            setattr(unistream, attr_name, getattr(stream, attr_name))

    # modify the write method to de-escape
    unistream.write = lambda b: stream.write(unescape(b, unistream.encoding))

    return unistream

def runs_in_ipython():
    '''Check if we are in IPython.'''
    import __builtin__
    return '__IPYTHON__' in __builtin__.__dict__ and \
           __builtin__.__dict__['__IPYTHON__']
