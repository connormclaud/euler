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
# Each new term in the Fibonacci sequence is generated by
# adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.

def fibonacci_sequence(stop_value = 4000000):
    '''Fibonacci sequence generator'''
    previous = 1
    yield previous
    current = 2
    while current <= stop_value:
        previous, current = current, previous + current
        yield previous

sum = reduce(lambda x, y: x + y
             if not y % 2 else x, fibonacci_sequence(), 0)

print 'The sum of the even-valued terms in the Fibonacci' +\
    ' sequence whose values do not exceed four million is %s' % sum
