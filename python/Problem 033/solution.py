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
# Find denominator of product of all possible two digit fractions where
# we can cancel one digit without changing fraction value
# Solution:
# more nested loops

def can_cancel():
    for cancelling in range(0, 10):
        for i in range(1, 10):
            for j in range(1, 10):
                for a in (10*i + cancelling, 10*cancelling + i):
                    for b in (10*j + cancelling, 10*cancelling + j):
                        if a < b and a / b == i / j:
                            yield a, b


def gcd(a, b):
    ''' greatest common divisor by Euclid's algorithm
    '''
    while b:
        a, b = b, a % b
    return a


print([i for i in can_cancel()])
numerator = 1
denominator = 1
for a, b in can_cancel():
    numerator *= a
    denominator *= b
answer =  denominator // gcd(numerator, denominator)
print('Denominator of product of found fractures is', answer)
#
