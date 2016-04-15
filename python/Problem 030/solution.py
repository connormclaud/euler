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
# Find the sum of all the numbers that can be written
# as the sum of sixth powers of their digits.
# Solution:
# brute force

max_power = 6
upper_limit = 3 * 10 ** max_power

def power_sum(number, power):
    sum = 0
    while number:
        digit = number % 10
        number = number / 10
        sum += digit ** power
    return sum

print sum(i for i in xrange(10, upper_limit) if i == power_sum(i, max_power))
#
