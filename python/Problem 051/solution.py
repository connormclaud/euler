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
# Prime digit replacement
# Find the largest prime which, by replacing part of the number
# (not necessarily adjacent digits) with the same digit,
# is part of an eight prime value family
# Solution:
# Generate primes with three repeated digits
# for each prime generate family and check length
from collections import Counter


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


def primes_guess_set(limit=999999, digit_count=3, prime_length=6):
    def have_repeated(number):
        counter = Counter(str(number))
        digit, count = counter.most_common(1)[0]
        return count == digit_count and digit in ('0', '1', '2')
    primes_sieve = sieve(limit)
    guess_gen = (
        i for i in primes_gen(primes_sieve) if have_repeated(i)
        and len(str(i)) == prime_length)
    primes_set = {i for i in primes_gen(primes_sieve)}
    return guess_gen, primes_set


def find(family_length=8):
    guesses, primes_set = primes_guess_set()
    for guess in guesses:
        counter = Counter(str(guess))
        digit, count =counter.most_common(1)[0]
        family = (list(filter(
            lambda x: int(x) in primes_set and x[0] != '0',
            (str(guess).replace(digit, str(i)) for i in range(10)))))
        if len(family) == family_length:
            return [int(i) for i in family]


print('The largest prime which, by replacing part of the number '
      'with the same digit, is part of an eight prime value family',
      max(find()))
