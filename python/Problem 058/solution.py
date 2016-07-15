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
# Spiral primes

# Solution:

def diagonal_values():
    last_value = 1
    increment = 0
    while True:
        increment += 2
        corners = [last_value + increment * i for i in range(1, 5)]
        last_value = corners[-1]
        yield corners


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


def prime_fracture():
    diagonal = diagonal_values()
    count = 1
    primes = 0
    length = 1
    while True:
        length += 2
        values = next(diagonal)
        count += 4
        primes += sum(1 for i in values if is_pseudo_prime(i))
        yield length, primes / count


def find():
    return next(x for x in prime_fracture() if x[1] < 0.09)


print('Spiral with side length of %s have %0.2f primes factor '
      'on diagonal' % find())
