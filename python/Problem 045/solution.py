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
# Find large hexagonal number which is also triangel and pentagonal
# Solution:
#
def is_pentagonal(number):
    r = ((24 * number + 1) ** 0.5 + 1) / 6
    return r.is_integer()

def is_triangle(number):
    r = ((8 * number + 1) ** 0.5 - 1) / 2
    return r.is_integer()


def hexagonal(n):
    return n * (2 * n - 1)


def find():
    for i in range(10000000):
        hex_number = hexagonal(i)
        if is_pentagonal(hex_number) and is_triangle(hex_number):
            yield hex_number


print('Hexagonal number is', max(find()))
