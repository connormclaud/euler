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
# Find pentagonal number pair which sum and difference also
# pentagonal number and difference minimized
# Solution:
#
def is_pentagonal(number):
    r = ((24 * number + 1) ** 0.5 + 1) / 6
    return r.is_integer()


def pentagonal(n):
    return n * (3 * n - 1) // 2


def find():
    i = 1
    while True:
        i += 1
        a = pentagonal(i)
        for j in range(i, 0, -1):
            b = pentagonal(j)
            if (is_pentagonal(a + b) and is_pentagonal(a - b)):
                return a, b

print('Pentagonal number pair is', find())
