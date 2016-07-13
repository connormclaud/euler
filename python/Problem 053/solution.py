#!/usr/bin/python
# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


# Task description:
# How many combinations from 100 is greater that 1 sextillion
# Solution:
from math import factorial

SEXTILLION = 10 ** 21

def combinations(n, r):
    result = factorial(n) / (factorial(r) * factorial(n -r))
    return int(result)


def find(limit=SEXTILLION):
    return sum(1 for i in (
        combinations(n, r) for n in range(1, 101) for r in range(1, n + 1))
     if i > limit)


print('There are %s combinations from 100 which is '
      'greater that 1 sextillion ' % find())
