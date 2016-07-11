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
# Find four consecutive integers to have four distinct prime factors.
# Solution:
# exhaustive enumeration

def sieve(limit=200000):
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



def prime_factors(number, primes):
    # step A1
    k = next(primes)
    n = number
    quotient = number
    while(quotient > k):
        # step A2
        if(n == 1):
            return
        # step A3
        quotient = n // k
        remainder = n % k
        # step A4
        if(remainder == 0):
            # step A5
            prime_factor = k
            yield prime_factor
            n = quotient
            # return to step A2
        else:
            # step A6
            k = next(primes)
            # return to step A3
    # step A7
    prime_factor = n
    yield prime_factor


def find():
    primes_sieve = sieve()
    consecutive = 4
    previous = 1
    sequence = 0
    for i in range(2, 200000):
        current = len(set(prime_factors(i, primes_gen(primes_sieve))))
        if previous == current and current == consecutive:
            sequence += 1
        else:
            sequence = 1
        previous = current
        if sequence == consecutive:
            return list(range(i - sequence + 1, i + 1))


print('Four consecutive numbers with four distinct prime factors are', find())
