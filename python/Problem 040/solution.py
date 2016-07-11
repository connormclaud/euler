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
# Find product of 10, 100, 1000 .., 10000000 digit of Champernowne's constant
# Solution:
# Generate constant, multiply digits, generator magic

from itertools import islice, chain, count
import operator
from functools import reduce


constant = chain.from_iterable(str(i) for i in count(0))
indeses = [10**i for i in range(8)]
part = islice(constant, max(indeses) + 1)
answer = reduce(operator.mul, (
    int(digit) for index, digit in enumerate(part) if index in indeses))

print('The product of certain digits of Champernowne constant is', answer)
