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
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.
# Solution:


def is_same_digits(number, anothers):
    return all(sorted(str(number)) == sorted(str(another))
               for another in anothers)


def find():
    return (i for i in range(1, 10 ** 6) if is_same_digits(
        i, (i * k for k in range(2, 7))))

print('Double of the smallest integer such that 2x, 3x, 4x, 5x, and 6x,'
      'contain the same digits is', next(find()) * 2)
