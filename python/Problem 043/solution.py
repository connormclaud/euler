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
# Find all pandigital numbers with interesting divisibility property
# Solution:
#
from itertools import permutations


def generate_pangititals():
    for item in permutations('0123456789'):
        if item[0] == '0':
            continue
        yield int("".join(str(i) for i in item))


def check_property(number):
    little_primes = [2, 3, 5, 7, 11, 13, 17]

    return all(int(str(number)[1 + i: 4 + i]) % little_primes[i] == 0
              for i in range(len(little_primes)))

def find():
    return (pandigital for pandigital in generate_pangititals()
            if check_property(pandigital))

print('Pandigital with interesting property are', list(find()))
