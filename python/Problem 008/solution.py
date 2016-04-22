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
# Find subarray of 42 elements which product
# is a maximum in 100000 element array


import random

from functools import reduce

# generate random array
digits = 100000
array = [int(10 * random.random()) for i in range(digits)]

elements = 42
max_value = 0
max_start = 0

# straightforward algorithm.
for index, item in enumerate(array):
    if index + elements > len(array):
        break
    # calculate a product of next elements
    product = reduce(lambda x, y: array[y + index] * x, range(elements), 1)
    if product > max_value:
        # if it is a maximum, remember it
        max_value = product
        max_start = index
# print the product
print(('The %s adjacent items in the %s-member array'
    ' that have the greatest product are: ') % (elements, digits))
print(' x '.join([str(array[x + max_start]) for x in range(elements)]), end=' ')
print('=', end=' ')
print(max_value)
