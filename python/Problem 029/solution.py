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
# How many distinct terms are in the sequence generated
# by a**b for 2 ≤ a ≤ 1000 and 2 ≤ b ≤ 1000?

# Solution:
# brute force oneliner
limit = 1000

answer = len(
    {
        a**b for a in xrange(2, limit + 1)
        for b in xrange(2, limit + 1)
    }
)
print 'There are %s distinct items in sequence' % answer
#
