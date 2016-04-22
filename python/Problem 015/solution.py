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
# Starting in the top left corner of a grid,
# and only being able to move to the right and down
# How many such routes are there through a 200×200 grid?

# Solution:
# According to http://mathworld.wolfram.com/LatticePath.html
# The number of paths of length a+b from the origin (0,0) to a point (a,b)
# which are restricted to east and north steps
# is given by the binomial coefficient (a+b; a).
#

def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n - i + 1) // i
    return result

answer = binomial_coefficient(400, 200)
print('There are {0} routes through a 200×200 grid'.format(answer))
