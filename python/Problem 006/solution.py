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
# Find the difference between the sum of the squares
# of the first one hundred thousand natural numbers and the square of the sum.

# sum of squares and a sum of consequitive numbers are basically
# arithmetic progressions with known formulas. Let's use them

limit = 100000


def sum_of_squares(limit):
    ''' formula is n(n+1)(2n+1)/6
    '''
    return limit * (limit + 1) * (2 * limit + 1) // 6


def square_of_sum(limit):
    ''' formula of sum is n(n+1)/2
    '''
    return (limit * (limit + 1) // 2) ** 2

difference = square_of_sum(limit) - sum_of_squares(limit)

print('The difference between the sum of the squares of the first '
      '{0} consequitive numbers and the square of the sum is {1}'.format(
          limit, difference))
