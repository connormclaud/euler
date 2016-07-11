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
# Disprove Christian Goldbach odd congecture
# Solution:
# Generate list of primes.
# Distract from odd number prime
# Check whether the difference is twice the square

def is_twice_the_square(number):
    r = (number / 2) ** 0.5
    return r.is_integer()


def sieve(limit=10000):
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


def primes(sieve):
    yield from (number for number,
                is_composite in enumerate(sieve) if not is_composite)


def check(number, sieve):
    return any(is_twice_the_square(number - prime) for prime in primes(sieve)
               if prime <= number)


def find():
    primes_sieve = sieve()
    for number in range(3, 10000, 2):
        if not check(number, primes_sieve):
            yield number

print('Number %s is not sum of prime and double square' % max(find()))
