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
# sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) infinite fraction
# In the first ten-thousand expansions, how many fractions
# contain a numerator with more digits than denominator?
# Solution:
# Knowing fraction from previous expansion we can use the formula
# numerator_next = numerator_previous + 2 * denominator_previous
# denominator_next = numenator_previous + denominator_previous

from itertools import islice
from math import log


def square_two_approximation():
    numerator, denominator = 3, 2
    yield numerator, denominator
    while True:
        numerator, denominator = (numerator + 2 * denominator,
                                  numerator + denominator)
        yield numerator, denominator


def digit_count(number):
    return int(log(number, 10)) + 1


def find():
    return sum(1 for n, d in islice(square_two_approximation(), 100001)
                if digit_count(n) > digit_count(d))


print('Number of fractions for first one hundred thousand expansions '
      'where numerator have more digits is', find())
