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
# Consecutive prime sum which is prime below 10 millions
#
# Solution:
# Exchaustive enumeration.
# Minor optimization (precalculate all sums)

from itertools import accumulate, takewhile

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


def primes_sum_set(limit):
    def accumulate_sum():
        return accumulate(takewhile(lambda x: x <= limit,
                                    primes_gen(primes_sieve)))

    def primes_set():
        return {prime for prime in primes_gen(primes_sieve)}

    primes_sieve = sieve(limit)

    return accumulate_sum(), primes_set()


def find(limit=10000000):
    prime_sum, prime_set = primes_sum_set(limit)
    prime_sum = list(prime_sum)
    for i in range(len(prime_sum), 0, -1):
        if prime_sum[i - 1] > limit:
            continue
        for j in range(len(prime_sum)):
            guess = prime_sum[i - 1] - prime_sum[j]
            if guess in prime_set and guess <= limit:
                yield i - j - 1, guess


print('There are %s consecutive primes which sum is prime (%s)' % next(find()))
