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
# Ordered fractions
# Solution:
# Generate Farey neighbors


def search(limit=100):
    previous = (2, 5)
    current = (3, 7)
    order = 8
    while order < limit:
        previous = (previous[0] + current[0], previous[1] + current[1])
        order = previous[1] + current[1]

    return previous


def find(limit=10 ** 8):
    return search(limit)


print('Numerator of the fraction immediately to the left of 3/7 is', find()[0])
