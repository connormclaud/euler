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
# How many different ways can £50 be made using any number of coins?

# Solution:
# Number partitioning problem
# Algorithm is the following
# http://math.stackexchange.com/a/245615
# coefficient of x*200 in the power series for
# 1/((1−x)(1-x**2)(1−x**5)(1−x**20)(1−x**50)(1−x**100)(1-x**200)

banknote = 50
size = banknote * 100 + 1
ways = [0 for i in range(size)]
ways[0] = 1

denominations = (1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000)

for coins in (coin for coin in denominations if coin < size):
    for i in range(size - coins):
        ways[i + coins] += ways[i]

answer = ways[-1]
print('There are {0} possible ways to make change for £{1}'.format(
    answer, banknote))
