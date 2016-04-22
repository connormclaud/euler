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
# Evaluate the sum of all the amicable numbers under 20000.

# Solution:
#115818
# There is efficient solution for generating large pairs
# http://www.ams.org/journals/mcom
# /1986-47-175/S0025-5718-1986-0842142-3/home.html

# but here bruteforce is enough


def proper_divisors(number):
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            yield i


def amicable_pairs(stop=2000):
    for i in range(2, stop):
        candidate = sum(proper_divisors(i))
        if (i > candidate and candidate != i
            and sum(proper_divisors(candidate)) == i):
            yield candidate, i

sum_pairs = sum(sum(pair) for pair in amicable_pairs(20000))
print('The sum of all amicable numbers under 20000 is', sum_pairs)
#
