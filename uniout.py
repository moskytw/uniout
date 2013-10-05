#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.2.2'

import sys
from _uniout import Uniout

def runs_in_ipython():
    import __builtin__
    return '__IPYTHON__' in __builtin__.__dict__ and \
           __builtin__.__dict__['__IPYTHON__']

if runs_in_ipython():
    from IPython.utils import io
    io.stdout = Uniout(sys.stdout)
    io.stderr = Uniout(sys.stderr)
else:
    sys.stdout = Uniout(sys.stdout)
    sys.stderr = Uniout(sys.stderr)
