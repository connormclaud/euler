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
# Find the sum of all primes below 2000000

limit = 20000000
sqrt_limit = int(limit**0.5) + 1

# Eratosphenes sieve
# False means prime number
sieve = [True, True, False] + [
    False if x % 2 else True for x in xrange(3, limit)]

for candidate in xrange(3, sqrt_limit, 2):
    if not sieve[candidate]:
        # found prime number
        # mark all composites where found prime is a factor
        i = 2
        while (i*candidate < limit):
            sieve[i*candidate] = True
            i += 1

sum_primes = sum(map(lambda x: x[0] if not x[1] else 0, enumerate(sieve)))
print 'Sum of all primes below %s is %s' % (limit, sum_primes)
