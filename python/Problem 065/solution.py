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
# Continued fraction for e

# Solution:
# http://oeis.org/A003417
# a(3n)=2n, a(1)=2, a(n)=1 else (i.e., for n>1, not multiple of 3)
# https://oeis.org/A007676
# numerator n: n(k) = a(k) * n(k-1) + n(k-2)
# n(1) = 2; n(2) = 3


def find(limit=100):
    previous = 1
    numerator = 2
    for i in range(2, limit + 1):
        temp = previous
        fraction = 2 * (i // 3) if i % 3 == 0 else 1
        previous = numerator
        numerator = fraction * previous + temp
    return(numerator)


def digit_sum(number):
    return sum(int(digit) for digit in str(number))

print('Digit sum for 1000th continued fraction '
      'numerator for e is', digit_sum(find(1000)))
