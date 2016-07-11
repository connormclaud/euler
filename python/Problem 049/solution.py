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
# Find sequence of primes which are permutaion of one another
# and fall apart equally from each other
# Solution:
#

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


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


def find():
    primes = {i for i in primes_gen(sieve())}
    distance = 3330
    for i in range(999, 10000):
        second = i + distance
        if not is_permutation(i, second):
            continue
        third = second + distance
        if not is_permutation(second, third):
            continue
        if i in primes and second in primes and third in primes:
            yield i, second, third


print('Found sequences are', list(
    map(lambda x: "".join(str(i) for i in reversed(x)),
        find()))[::-1])
