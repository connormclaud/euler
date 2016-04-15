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
# What is the sum of the digits of the number 100000!


# Solution:
# this problem is oneliner in python
# we convert number to str and iterate over all
# digits to sum them up
#
from math import factorial

number = 100000

def digit_sum(n):
    return sum(map(int, str(n)))

answer = digit_sum(factorial(number))

print 'The sum of the digits of the number %s! is' % number, answer
