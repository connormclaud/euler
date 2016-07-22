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
# Find the minimum total from top to bottom of the triangle from file:

# Solution:
# It is possible to solve this using shortest paths in directed acyclic graphs
# in linear time, but I like more dynamic programming approach when we go
# from bottom to top and eliminate all impossible paths

# data structure: Here 2d array is enough. We imply graph with implicit edges


def read_data(filename='p067_triangle.txt'):
    with open(filename, 'r') as f:
        content = f.read()
    data = [[int(s) for s in line.split()] for line in content[1:].splitlines()]
    return data


def find():
    data = read_data()
    # go bottom to top
    reverse = data[::-1]
    while len(reverse) > 1:
        for i, lst in enumerate(reverse[1:2], 1):
            for position, item in enumerate(lst):
                left = reverse[i - 1][position]
                right = reverse[i - 1][position + 1]
                # eliminate minimum path by merging
                reverse[i][position] = min(item + left, item + right)

        # make problem one line shorter
        del reverse[0]
    return reverse[0][0]


print('Minimum total from top to bottom of the triangle is {0}'.format(
    find()))
