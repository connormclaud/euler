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
# Maximum integral perimeters solutions
# Solution:
# exhaustive enumeration


def try_all(limit=1000):
    # count all integral perimeters
    perimeters = dict()
    for a in range(1, limit):
        for b in range(a, limit):
            c = (a ** 2 + b ** 2) ** 0.5
            if c.is_integer():
                perimeter = a + b + int(c)
                if perimeter in perimeters:
                    perimeters[perimeter] += 1
                else:
                    perimeters[perimeter] = 1
    return perimeters

answer = try_all()

print('Integral perimeter with maximum number of different '
      'right angle triangles is {0}'.format(max(answer, key=answer.get)))
