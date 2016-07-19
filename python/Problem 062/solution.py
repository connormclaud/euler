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
# Cubic permutations

# Solution:
#
from collections import defaultdict


def generate_cubes():
    return (i ** 3 for i in range(1, 100000))


def find():
    perms = defaultdict(list)
    for cube in generate_cubes():
        perm = "".join(sorted(str(cube)))
        perms[perm].append(cube)
        if len(perms[perm]) == 6:
            yield perms[perm]


print('The smallest cube for which exactly six permutations'
      ' of its digits are cubes is', min(min(find(), key=min)))
