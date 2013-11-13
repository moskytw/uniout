#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from _uniout import make_unistream, runs_in_ipython

__version__ = '0.3.3'

if runs_in_ipython():
    from IPython.utils import io
    io.stdout = make_unistream(sys.stdout)
    io.stderr = make_unistream(sys.stderr)
else:
    sys.stdout = make_unistream(sys.stdout)
    sys.stderr = make_unistream(sys.stderr)
