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
# Prime pair set

# Solution:
#
from itertools import islice, combinations
from collections import defaultdict


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


def concat(other, another):
    return [int(str(other) + str(another)), int(str(another) + str(other))]


def is_prime(sieve, number):
    if number < len(sieve):
        return not sieve[number]
    return is_pseudo_prime(number)


def is_pseudo_prime(number):
    ''' Rabin-Miller primarity test '''
    if (number <= 1):
        return False
    if (number == 2):
        return True
    if (number % 2 == 0):
        return False
    if (number < 9):
        return True
    if (number % 3 == 0):
        return False
    if (number % 5 == 0):
        return False

    for witness in [2, 3]:
        if (rabin_miller_check(witness, number)):
            return False;

    return True;


def rabin_miller_check(witness, number):
    times = 0
    exponent = number - 1
    while ((exponent & 1) == 0):
        times += 1
        exponent >>= 1

    check = modular_exp(witness, exponent, number);

    for i in range(0, times):
        next_check = check * check % number;
        if ((next_check == 1) and (check != 1) and (check != (number - 1))):
            return True;m
        check = next_check;

    if (check != 1):
        return True;
    return False;


def modular_exp(base, exponent, modulus):
    result = 1
    k = 0
    while ((exponent >> k) > 0):
        k += 1

    for i in range(k - 1, -1, -1):
        result = result * result % modulus;
        if (((exponent >> i) & 1) > 0):
            result = result * base % modulus

    return result


def concat_prime_pairs(prime_sieve, prime_set):
    result = defaultdict(set)
    for other, another in combinations(prime_set, 2):
        if all(is_prime(prime_sieve, i) for i in concat(other, another)):
            result[other].add(another)
            result[another].add(other)
    return result


def intersections(pairs):
    for key in pairs:
        for subkey in pairs[key]:
            intersection = pairs[key] & pairs[subkey]
            for interkey in intersection:
                deeper = intersection & pairs[interkey]
                for deepkey in deeper:
                    result = deeper & pairs[deepkey]
                    if len(result):
                        yield (key, subkey, interkey,
                               deepkey, *(i for i in result))


def find():
    prime_sieve = sieve(10 ** 7)
    prime_set = {prime for prime in islice(primes_gen(prime_sieve), 1290)}
    pairs = concat_prime_pairs(prime_sieve, prime_set)
    return min(intersections(pairs), key=sum)


print('set of five primes for which any two primes'
      ' concatenate to produce another prime is', find())
