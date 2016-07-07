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
# Find the sum of all numbers, less than one million,
# which are palindromic in base 10 and base 2.

from collections import deque


def larger_palindromes(palindrome):
    yield '0' + palindrome + '0'
    yield '1' + palindrome + '1'


def base_palindromes():
    yield '0'
    yield '1'
    yield from larger_palindromes('')


def all_palindromes(limit=40):
    queue = deque(list(base_palindromes()))
    while len(queue):
        item = queue.popleft()
        if len(item) > limit:
            break
        yield item
        for pal in larger_palindromes(item):
            queue.append(pal)


def is_palindrome(number):
    if len(number) in (0, 1):
        return True
    return number[0] == number[-1] and is_palindrome(number[1:-1])

result = filter(
    lambda x: is_palindrome(str(x)),
    (int(pal, 2) for pal in all_palindromes() if pal[0] == '1'))
print('Sum of all numbers which are palindromic in base 10 and 2 below %s '
      'binary digits is %s' % (40, sum(result)))
#
