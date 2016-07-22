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
# Solve magic 5-gon

# Solution:
from itertools import permutations
from collections import deque


def identity(gon, lines):
    head = min(enumerate(lines), key=lambda x: gon[x[1][0]])
    heads = deque(lines)
    heads.rotate(-head[0])
    result = "".join([str(gon[item]) for line in heads for item in line])
    return result


def check_if_magic(gon, lines):
    line_sum = [sum(gon[item] for item in line) for line in lines]
    line_set = set(line_sum)
    return len(line_set) == 1


def find():
    gon = list(range(1, 11))
    lines = [[0, 1, 2], [3, 2, 4], [5, 4, 6], [7, 6, 8], [9, 8, 1]]
    for guess in permutations(gon[:-1]):
        # minor optimization: longest element on head
        guess = (gon[-1],) + guess
        if check_if_magic(guess, lines):
            ident = identity(guess, lines)
            if len(ident) == 16:
                yield ident


print('Minimum string for magic 5gon is', min(int(i) for i in find()))
