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
# Find the product of Pythagorean triple which sum is 10000000

# according to Euclid's formula:
# a = m^2 - n^2 , b = 2mn ,c = m^2 + n^2
# hence the sum is 2m^2 + 2mn, therefore m(m+n) equal to half of the sum

sum_of_triple = 10000000
if sum_of_triple % 2:
    raise Exception('No possible solutions')
half = sum_of_triple // 2


def euclid_numbers(half):
    ''' now we should found the solution for m and n in natural numbers
    '''
    for i in range(1, half):
        if sum_of_triple % i:
            # should be factor of sum
            continue
        m = i
        n = half // m - m
        if m < n:
            continue
        return m, n


def euclid_triple(m, n):
    ''' calculate triplet from euclid formula
    '''
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    return a, b, c

m, n = euclid_numbers(half)

a, b, c = euclid_triple(m, n)

if a**2 + b**2 != c**2:
    raise Exception("Logic is broken. Found numbers aren't Pythagorean triple")

print('Product of Pythagorean triple '
      'which sum is %s equal to %s\nTriple is %s | %s | %s' % (
          sum_of_triple, a*b*c, a, b, c
      ))
