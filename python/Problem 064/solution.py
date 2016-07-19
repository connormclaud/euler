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
# Continued fraction

# Solution:
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
# iterative algorithm
from math import floor


def continued_fractions(number):
    result = []
    fraction = ()
    m = 0
    d = 1
    a0 = number ** 0.5
    if a0.is_integer():
        return [a0, None]
    a0 = floor(a0)
    a = a0
    result.append(a)
    while True:
        m = d * a - m
        d = (number - m ** 2) / d
        a = floor((a0 + m) / d)
        fraction += (a,)
        if a == 2 * a0:
            break
    result.append(fraction)
    return result


def find_periods(limit=10000):
        return (period for period in (
            fraction(i)[1] for i in range(2, limit))
                if period is not None)


def odd(periods):
    yield from (period for period in periods if len(period) % 2)


def find(limit=80000):
    periods = find_periods(limit)
    return odd(periods)


print('There are %s continued fractions for numbers '
      'below 80000 with odd period' % sum(1 for i in find()))
