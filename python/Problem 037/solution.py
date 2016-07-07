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
# Find the sum of all two-side truncateble primes
# Solution:
# Find all primes below 1 million
# Truncate and check whether we found one


def sieve(limit=1000000):
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


def is_truncatable(number, sieve):
    def is_left_truncatable(number):
        if len(str(number)) == 1:
            return not sieve[number]
        return not sieve[number] and is_left_truncatable(int(str(number)[1:]))

    def is_right_truncatable(number):
        next_check = number // 10
        if not number:
            return True
        return not sieve[number] and is_right_truncatable(next_check)
    return (
        is_left_truncatable(number) and
        is_right_truncatable(number))


def find():
    primes_sieve = sieve()
    return (
        number for number, is_not_prime in enumerate(
            primes_sieve) if not is_not_prime and
        is_truncatable(number, primes_sieve))

print('The sum of all two-side truncateble primes is %s' % sum(find()))
