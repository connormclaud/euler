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
# How many circular primes before 1 hundred thousand
# Note: There are 13 circular primes befor hundred
# Solution:
# Walter Schneider:
# 1. Recursively generate all possible strings of length n.

# Only the digits 1, 3, 7 and 9 have to be considered. I use strings
# (not numbers) because this is much faster. Because we search only for the
# least number in each cycle the recursion can be speeded up by some easy
# tests. For example, digits 2 to n cannot be smaller than the first digit.
# (Therefore most of the running time is spent when the first digit is one!)

# 2. For each string generated in 1. of length n determine the whole cycle
# and test if the original string is the least one in the cycle. Note that
# we still work with strings not numbers.

# 3. For each string in the cycle convert the string to a big integer and
# test for a small factor. I use the LiDIA bigint library and make a
# divisibility test by all primes less than 100.

# 4. Not too much numbers are left at this step. For each number in the cycle
# make a fermat test.
import random
import itertools as it
from collections import deque


def fermat_test(n, k=1):

    # Fermat Primality Test

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):
        a = random.randint(1, n-1)

        if pow(a, n-1) % n != 1:
            return False
    return True


def small_test(number):
    little_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97, 101]
    for prime in little_primes:
        if number == prime:
            return True
        if number % prime == 0:
            return False
    return True

def generate_guesses():
    return (
        "".join(i) for j in range(3, 6)
        for i in it.product('1379', repeat=j) if min(i) == i[0])

def generate_circles(s):
    d = deque(s)
    return {(
        d.rotate(), "".join(d))[1] for i in range(len(d))}

def check(number, method):
    memo = check.memo.get(method, dict())
    check.memo[method] = memo
    for circle in generate_circles(number):
        if circle in memo:
            return memo[circle]
        if not method(int(circle)):
            memo[circle] = False
            return False
    for circle in generate_circles(number):
        memo[circle] = True
    return True

check.memo = dict()

def find():
    for number in generate_guesses():
        if not check(number, small_test):
            continue
        if not check(number, fermat_test):
            continue
        yield from generate_circles(number)

circular_primes = {int(i) for i in find()}
print("There are %s circular primes before %s" % (
    len(circular_primes) + 13, 100000) )


#
