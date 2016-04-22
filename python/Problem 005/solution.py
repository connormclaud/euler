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
# Compute least common multiplier for all integers from 1 to 160

limit = 160
# we can decrease number of calculations by dropping first half of input.
input = range(limit//2 + 1, limit + 1, 1)


def gcd(a, b):
    ''' greatest common divisor by Euclid's algorithm
    '''
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    ''' least common multiple for two numbers
    '''
    return a // gcd(a, b) * b

result = 1
for i in input:
    result = lcm(result, i)

print("the smallest positive number that is evenly divisible"
      " by all of the numbers from 1 to {0} is {1}".format(limit, result))
