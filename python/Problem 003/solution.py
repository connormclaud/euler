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
# What is the largest prime factor of the number 269685300662584836649?

# we will use simple factorizing algorithm from Knuth's The art of computer
# programming Vol2 4.5.4
# Factoring into Primes Algorithm A (Factoring by division)
# This algorithm is simple but not efficient for large number.

# we need prime numbers to divide for. Fortunately, this algorithm will work
# even if a list of numbers contains some numbers which are not prime
# So we can add 2 and 4 for items after first three. This list will contain
# all prime numbers and more.
from math import sqrt
import collections


def prime_like_number_generator(stop_value=500000):
    for i in [2, 3, 5]:
        item = i
        yield item
    while(item < stop_value):
        item += 2
        yield item
        item += 4
        yield item

number = 269685300662584836649
# largest prime factor can't be greater than square of N
primes = prime_like_number_generator(sqrt(number))


def prime_factors(number):
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

# get last element from generator
largest_prime_factor = collections.deque(prime_factors(number), maxlen=1).pop()
print('The largest prime factor of'
      ' the number {0} is {1}'.format(number, largest_prime_factor))
