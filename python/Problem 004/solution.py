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

# Find the largest palindrome made from the product of two 4-digit numbers.

#usually person brute force this by iterating all products of
# four digits numbers and checking whether it is palindrome or not
# I don't like this approach. I will generate all 8-digit palindromes
# then factoring it


digits = 4
maximum = 10**(digits) - 1
minimum = 10**(digits - 1)

def palindroms_generator():
    # start from largest palindromes as in description
    for i in xrange(maximum, minimum - 1, -1):
        number = i
        palindrom = i
        # add reversed number to the end
        while number:
            palindrom *= 10
            palindrom += number % 10
            number = number / 10
        yield palindrom

def right_digit_factors(number):
    def is_right_digit(k):
        return maximum >= k >= minimum

    for i in xrange(maximum, minimum - 1, -1):
        quotient = number / i
        remainder = number % i
        if not remainder and is_right_digit(quotient):
            yield (i, quotient)
            break

for palindrom in palindroms_generator():
    if maximum**2 >= palindrom >= minimum**2:
        factors = list(right_digit_factors(palindrom))
        if factors:
            # we found it
            break

print "the largest palindrome made from " + \
    "the product of two %s-digit numbers is %s" % (digits, palindrom)
