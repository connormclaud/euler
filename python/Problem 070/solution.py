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
# Totient permutation

# Solution:
# We need to minimize number of prime factors in order to find totient minimum
from itertools import combinations


def is_permutation(other, another):
    return sorted(str(other)) == sorted(str(another))


def phi(factor, another_factor):
    return (factor - 1) * (another_factor - 1)


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


def primes_gen(sieve):
    yield from (number for number,
                is_composite in enumerate(sieve) if not is_composite)


def find(limit=10000):
    return ((i * j / phi(i, j), i * j, i, j)
            for i, j in combinations(primes_gen(sieve(limit)), 2)
            if i * j < 10**8 and is_permutation(i * j, phi(i, j)))


print('Totient permutation with minumal n/phi is', min(find())[1])
