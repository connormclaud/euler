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
# sum of the numbers on the diagonals in spiral


# Solution:
# brute force,
# actually, it is possible to solve in constant time using math formula


def generate_spiral(dimension):
    spiral = [[0 for x in xrange(dimension)] for x in xrange(dimension)]
    i = dimension / 2
    j = i
    value = 1
    steps_left = 1
    steps_count = 1
    i_increment = 0
    j_incerement = 1
    while i < dimension and j < dimension:
        spiral[i][j] = value
        if steps_left <= 0:
            steps_left = steps_count
            steps_count += 0.5
            i_increment, j_incerement = -j_incerement, i_increment
        i += i_increment
        j += j_incerement
        value += 1
        steps_left -= 1
    return spiral[::-1]

dim = 5001
spiral = generate_spiral(dim)

def diagonal_values(spiral, dimensions):
    for i in xrange(dimensions):
        yield spiral[i][i]
        if i != dimensions - i - 1:
            yield spiral[i][dimensions - i - 1]

sum_values = 0

answer = sum(diagonal_values(spiral, dim))
print 'Sum of diagonal numbers of spiral %sx%s is' % (dim, dim), answer
#
