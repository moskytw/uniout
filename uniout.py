#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.3'

from _uniout import Uniout, runs_in_ipython
import sys

if runs_in_ipython():
    from IPython.utils import io
    io.stdout = Uniout(sys.stdout)
    io.stderr = Uniout(sys.stderr)
else:
    sys.stdout = Uniout(sys.stdout)
    sys.stderr = Uniout(sys.stderr)
