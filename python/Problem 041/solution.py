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
# Find the sum of all 7 digit pandigital primes
# Solution:

def sieve(limit=7654321):
    ''' Eratosphenes sieve '''
    sieve = [True, True, False] + [
        False if x % 2 else True for x in range(3, limit)]
    for candidate in range(3, int(limit ** 0.5) + 1, 2):
        if not sieve[candidate]:
            # found prime number
            # mark all composites where found prime is a factor
            i = 2
            while (i*candidate < limit):
                sieve[i*candidate] = True
                i += 1

    return sieve


def is_pandigital(number, length):
    digits = [False for i in range(10)]
    while number:
        number, digit = number[1:], int(number[0])
        if not digits[digit]:
            digits[digit] = True
        else:
            return False
    return all(digits[1:length + 1])


def find():
    prime_sieve = sieve()
    return sum(number for number, is_composite in enumerate(
        prime_sieve) if not is_composite and len(str(number)) == 7
               and is_pandigital(
            str(number), len(str(number))))


print('Sum of 7 digit pandigital primes is', find())
