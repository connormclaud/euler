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
# Work out the first ten digits of the sum
# of the one-hundred 50-digit numbers.


# Solution:
# solution is typical one-liner
# generating random input is trickier

import random

random_numbers = [
    int(random.randrange(10**50, 10**51 - 1)) for i in range(100)]

numbers = "\n".join([str(x) for x in random_numbers])
numbers_sum = sum([int(line) for line in numbers.split('\n')])
print(('The first ten digits of the sum of the '
       'one-hundred 50-digit numbers is %s') % str(numbers_sum)[:10])
