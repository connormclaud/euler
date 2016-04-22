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
# What is the value of the first triangle number
# to have over 1000 divisors?

# Solution:
# brute force with O(n*sqrt(n)) complexity

MAX_DIVISORS = 1000


def nth_triangle(n):
    ''' According http://oeis.org/A000217
    T(n) = n(n+1)/2, as it basically sum of arithmetic progression
    '''
    return n * (n + 1) // 2


def divisors(number):
    ''' Number of divisors will be found by checking each number
    from 1 to sqrt(n) for having remainder
    '''
    answer = 0
    square = int(number**0.5)
    for i in range(1, square + 1):
        if not (number % i):
            answer += 2
    if square**2 == number:
        answer -= 1
    return answer


for i in range(100000):
    if divisors(nth_triangle(i)) > MAX_DIVISORS:
        print((
            'The value of the first triangle number '
            'to have over {0} divisors is {1}'.format(
                MAX_DIVISORS,
                nth_triangle(i))))
        break
