#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.2.2'

import sys
from _uniout import UniOut

def runs_in_ipython():
    import __builtin__
    return '__IPYTHON__' in __builtin__.__dict__ and \
           __builtin__.__dict__['__IPYTHON__']

if runs_in_ipython():
    from IPython.utils import io
    io.stdout = UniOut(sys.stdout)
    io.stderr = UniOut(sys.stderr)
else:
    sys.stdout = UniOut(sys.stdout)
    sys.stderr = UniOut(sys.stderr)
