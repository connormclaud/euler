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
# Find the longest recurring cycle in its decimal fraction part

# Solution:
# https://oeis.org/A051626
# contains algorithm in maple
# A051626 := proc(n) local lpow, mpow ;
#     if isA003592(n) then
#        RETURN(0) ;
#     else
#        lpow:=1 ;
#        while true do
#           for mpow from lpow-1 to 0 by -1 do
#               if (10^lpow-10^mpow) mod n =0 then
#                  RETURN(lpow-mpow) ;
#               fi ;
#           od ;
#           lpow := lpow+1 ;
#        od ;
#     fi ;
# end: # R. J. Mathar, Oct 19 2006

# isA003592 := proc(n)
#       if n = 1 then
#         true;
#     else
#         return (numtheory[factorset](n) minus {2, 5} = {} );
#     end if;
# end proc: # R. J. Mathar, Jul 16 2012

from math import sqrt


def prime_like_number_generator(stop_value=500000):
    for i in [2, 3, 5]:
        item = i
        yield item
    while(item < stop_value):
        item += 2
        yield item
        item += 4
        yield item

number = 10000000
# largest prime factor can't be greater than square of N
primes_list = list(prime_like_number_generator(sqrt(number)))


def prime_factors(number):
    # step A1
    primes = iter(primes_list)
    k = primes.next()
    n = number
    quotient = number
    while(quotient > k):
        # step A2
        if(n == 1):
            return
        # step A3
        quotient = n / k
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
            k = primes.next()
            # return to step A3
    # step A7
    prime_factor = n
    yield prime_factor

from itertools import takewhile

def has_factors2or5(n):
    return any(factor in (2, 5) for factor in takewhile(lambda x: x <= 5,
        prime_factors(n)))


def proc(n):
    mpow = 0
    lpow = 1
    if n == 1 or has_factors2or5(n):
        return 0
    while True:
        for mpow in xrange(lpow - 1, 0, -1):
            if (10**lpow - 10**mpow) % n == 0:
                return lpow - mpow
        lpow += 1

answer = max((proc(i), i) for i in xrange(1, 400))
print 'longest recurring cicle is %s digits in number 1/%s' % answer
#
