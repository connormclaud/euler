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
# Which starting number, under two million, produces the longest
# Collatz sequence chain?

# Solution:
# brute force algorithm

def chain_length(start):
    length = 0
    current = start
    while current > 1:
        if not current % 2:
            current /= 2
        else:
            current = current * 3 + 1
        length += 1
    return length

max_length = 0
max_number = 0
for i in xrange(2*10**6, 1, -1):
    length = chain_length(i)
    if length > max_length:
        max_length = length
        max_number = i

print ('Number, under two million, produces the longest '
       'Collatz sequence chain is %s' % max_number)
