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
# Find largest pandigital concatenation product
# Solution:
# Largest product should start from 9, hence our integer
# is 4 digit started from 9

def is_pandigital(number):
    digits = [False for i in range(10)]
    while number:
        number, digit = number[1:], int(number[0])
        if not digits[digit]:
            digits[digit] = True
        else:
            return False
    return all(digits)

def find():
    for i in range(9999, 0, -1):
        for j in range(2, 10):
            product = "".join(str(i * k) for k in range(1, j))
            if is_pandigital(product):
                return product

print('Largest concatenation product which is pandigital is {0}'.format(find()))
