#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint

lines = list(open('article.txt'))

print '# Before:'
print
pprint(lines)
print

ulines = [line.decode('utf-8') for line in lines]
print(ulines)
print
print

import uniout

print '# After:'
print
pprint(lines)
print
pprint(ulines)
