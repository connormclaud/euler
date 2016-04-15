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
# Find the sum of all the positive integers below 1000
# which cannot be written as the sum of two abundant numbers.

# Solution:
# generate set of abundant numbers
# sum all number which is not sum of any two numbers in set

def proper_divisors(number):
    for i in xrange(1, number / 2 + 1):
        if number % i == 0:
            yield i


def abundant_numbers(stop=200):
    for i in xrange(12, stop):
        if sum(proper_divisors(i)) > i:
            yield i


def not_sum(stop=200):
    abundant = set(abundant_numbers(stop))
    for i in xrange(1, stop):
        if not any((i - a in abundant for a in abundant)):
            yield i


print sum(not_sum(1000))
#
