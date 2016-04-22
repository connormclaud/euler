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
# Find the 100001th prime number

# lets do slow and inefficient implementation of Eratosphene sieve
from math import log

nth = 100001
result = 0


def estimate_prime(n):
    ''' according Knuth's Concrete Mathematics prime number estimation is
    Pn = n ln n + n ln ln n - n + n (ln ln n) / ln n + O( n/log n)
    this is overestimates
    '''
    prime = n * log(n) + n * log(log(n)) - n + n * (log(log(n))) / log(n)
    return prime

estimate = int(estimate_prime(nth))+1
sqrt_estimate = int(estimate**0.5)+1

# use Eratosphenes sieve
# False means prime number
sieve = [True, True, False] + [
    False if x % 2 else True for x in range(3, estimate)]
prime_count = 1
for candidate in range(3, sqrt_estimate, 2):
    if not sieve[candidate]:
        # found prime number
        prime_count += 1
        # mark all composites where found prime is a factor
        i = 2
        while (i * candidate < estimate - 1):
            sieve[i * candidate] = True
            i += 1

for candidate in range(sqrt_estimate, estimate):
    if not sieve[candidate]:
        prime_count += 1
        if prime_count == nth:
            result = candidate
            break

print('Found {0}th prime: \n{1}'.format(nth, result))
