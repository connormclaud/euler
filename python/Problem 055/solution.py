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
# Lychrel numbers candidates
# Solution:

def is_palindrome(number):
    if len(number) in (0, 1):
        return True
    return number[0] == number[-1] and is_palindrome(number[1:-1])


def lychrel_step(number):
    s = str(number)
    return int(s) + int(s[::-1])


def check_if_lychrel(number):
    for i in range(55):
        number = lychrel_step(number)
        if is_palindrome(str(number)):
            break
    else:
        return True
    return False


def find(limit=100000):
    return sum(1 for i in range(limit) if check_if_lychrel(i))

print('There are %s Lychrel number candidates below 100000' % find())
