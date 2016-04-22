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
# Find 3 millionth permutation of all digits in lexographic order
# Solution:
# one liner in python as itertools.permutations
# alredy produce it in lexographic order
from itertools import permutations, islice

answer = [
    "".join(item) for item in islice(
        permutations('0123456789'), 3000000, 3000001)][0]

print('3 millionth permutation of all digits is', answer)
#
