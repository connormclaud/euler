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
# Cyclical figurate numbers

# Solution:
#
from itertools import count, permutations

def triangle(n):
    return n * (n + 1) // 2


def square(n):
    return n ** 2


def pentagonal(n):
    return n * (3 * n - 1) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def heptagonal(n):
    return n * (5 * n - 3) // 2


def octagonal(n):
    return n * (3 * n - 2)


def four_digit_generator(formula):
    for i in count(1):
        number = formula(i)
        if number > 9999:
            break
        elif number < 1000:
            continue
        yield number


def numbers():
    return (set(four_digit_generator(formula)) for formula in (
        triangle, square, pentagonal, hexagonal, heptagonal, octagonal))


def find_chain():
    def chain_from(number, iterable):
        return {i for i in iterable if is_chain(number, i)}

    def is_chain(other, another):
        return another // 100 == other % 100

    def chain(number, *sequence):
        chain = [number]
        for other in chain_from(number, sequence[0]):
            for another in chain_from(other, sequence[1]):
                for x in chain_from(another, sequence[2]):
                    for y in chain_from(x, sequence[3]):
                        for z in chain_from(y, sequence[4]):
                            if is_chain(z, number):
                                yield number, other, another, x, y, z

    collections = tuple(numbers())
    for tri_number in collections[0]:
        for order in permutations(range(1, 6)):
            yield from chain(tri_number, *(collections[i] for i in order))


print('six cyclic 4-digit numbers for which each polygonal type are', max(
    find_chain()))
