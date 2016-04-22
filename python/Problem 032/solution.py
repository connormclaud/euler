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
# Find the sum of all products whose
# multiplicand/multiplier/product identity
# can be written as a 0 through 9 pandigital.
# Solution:
# I use permutation module to generate all possible
# multiplicand/multiplier pair and than check product

from itertools import permutations


def is_unusual(a, b):
    def check_digits(number, digits):
        while number:
            number, digit = number // 10, number % 10
            if not digits[digit]:
                digits[digit] = True
            else:
                return False
        return True
    digits = [False for i in range(10)]
    if (
            check_digits(a, digits) and
            check_digits(b, digits) and
            check_digits(a * b, digits)):
        return all(digits)
    else:
        return False


def gen_unusual():
    for digits in range(1, 6):
        for start in range(1, digits):
            for i in permutations('0123456789', digits):
                s = ("".join(i))
                a = int(s[:start])
                b = int(s[start:])
                if is_unusual(a, b):
                    yield a, b, a*b

unusual = {item[2] for item in gen_unusual()}
answer = sum(unusual)
print('Sum of all pandigital products is', answer)
