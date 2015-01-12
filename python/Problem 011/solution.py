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
# Find the greatest product of four numbers in grid 20x20 on any direction
import random

# generate random grid
length = 20
grid = [[
    int(100 * random.random()) for i in xrange(length)] for i in xrange(length)]
elements = 4

#straightforward algorithms. Just traverse grid and calculate products
def largest_product_in_grid(grid):
    largest_product = [0]
    largest_items = [None]

    def calculate_product():
        def product(items):
            return reduce(lambda x, y: x * y, items , 1)
        def check_largest(items, largest_product=largest_product,
            largest_items=largest_items):
            candidate = product(items)
            if candidate > largest_product[0]:
                largest_product[0] = candidate
                largest_items[0] = items[:]

        has_columns = column + elements <= length
        if has_columns:
            horizontal = map(
                lambda index: grid[row][column + index], xrange(elements)
            )
            check_largest(horizontal)
        has_rows = row + elements <= length
        if has_rows:
            vertical = map(
                lambda index: grid[row + index][column], xrange(elements)
            )
            check_largest(vertical)
        if has_rows and column >= elements:
            diagonal_backward = map(
                lambda index: grid[row + index][column - index],
                xrange(elements)
            )
            check_largest(diagonal_backward)
        if has_rows and has_columns:
            diagonal_forward = map(
                lambda index: grid[row + index][column + index],
                xrange(elements)
            )
            check_largest(diagonal_forward)

    for row, line in enumerate(grid):
        for column, cell in enumerate(line):
            calculate_product()

    return largest_items[0], largest_product[0]


print ('the greatest product of four adjacent numbers'
    '%s in the same direction is:%s') % largest_product_in_grid(grid)
