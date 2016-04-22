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


def has_factors2or5(n):
    return not (n % 2 or n % 5)


def proc(n):
    mpow = 0
    lpow = 1
    if n == 1 or has_factors2or5(n):
        return 0
    while True:
        for mpow in range(lpow - 1, 0, -1):
            if (10**lpow - 10**mpow) % n == 0:
                return lpow - mpow
        lpow += 1

answer = max((proc(i), i) for i in range(1, 400))
print('longest recurring cicle is %s digits in number 1/%s' % answer)
#
