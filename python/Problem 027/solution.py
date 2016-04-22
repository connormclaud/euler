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
# Find formula which produce maximum amount of successful primes


# Solution:
# brute force

limit = 2000
sqrt_limit = int(limit**0.5) + 1
formula_limit = 2000
# Eratosphenes sieve
# False means prime number
sieve = [True, True, False] + [
    False if x % 2 else True for x in range(3, limit)]

for candidate in range(3, sqrt_limit, 2):
    if not sieve[candidate]:
        # found prime number
        # mark all composites where found prime is a factor
        i = 2
        while (i * candidate < limit):
            sieve[i * candidate] = True
            i += 1

primes = set(i[0] for i in enumerate(sieve) if not i[1])


def formula(n, a, b):
    return n ** 2 + a * n + b

maximum = 0
max_a = -formula_limit - 1
max_b = -formula_limit - 1
for a in range(-formula_limit, formula_limit + 1):
    for b in range(-formula_limit, formula_limit + 1):
        for i in range(0, formula_limit):
            if formula(i, a, b) not in primes:
                if i > maximum:
                    maximum = i
                    max_a = a
                    max_b = b
                break
print("Formula (n**2 + %sn + %s) produces %s consecutive primes" % (
    max_a, max_b, maximum))
#
