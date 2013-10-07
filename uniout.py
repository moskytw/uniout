#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.3'

import sys
from _uniout import Uniout, runs_in_ipython

if runs_in_ipython():
    from IPython.utils import io
    io.stdout = Uniout(sys.stdout)
    io.stderr = Uniout(sys.stderr)
else:
    sys.stdout = Uniout(sys.stdout)
    sys.stderr = Uniout(sys.stderr)
