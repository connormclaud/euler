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
# Ordered fractions length
# Solution:
# Farey sequence length
from math import floor


def length(n):
    if n in length.memo:
        return length.memo[n]
    prefix = (n + 3) * n // 2
    other_sum = sum(length(floor(n / d)) for d in range(2, n + 1))
    result = prefix - other_sum
    length.memo[n] = result
    return result

length.memo = dict()

print('Farey millionth sequence length is', length(10 ** 6))
