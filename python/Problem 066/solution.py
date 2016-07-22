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
# Diophantine equation

# Solution:
# Solution through continued fraction approximation

from math import floor
from itertools import cycle


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


def approximation(number):
    fractions = continued_fractions(number)
    a0, rest = fractions
    old_h = a0
    old_k = 1
    yield old_h, old_k
    if rest is None:
        return
    h = a0 * rest[0] + 1
    k = rest[0]
    yield h, k
    fracts = cycle(rest)
    next(fracts)
    for a in fracts:
        temp_h = h
        temp_k = k
        h = a * h + old_h
        k = a * k + old_k
        yield h, k
        old_h = temp_h
        old_k = temp_k


def solve_equation(D):
    ''' x^2 - Dy^2 = 1 '''
    for x, y in approximation(D):
        if x ** 2 - D * y ** 2 == 1:
            return x, y


def find(limit=20000):
    for D in range(2, limit + 1):
        if (D ** 0.5).is_integer():
            continue
        try:
            solution = solve_equation(D)
        except:
            continue
        yield (solution, D)


print('minimal solutions of x for which the'
      ' largest value of x is obtained is', max(find())[-1])
