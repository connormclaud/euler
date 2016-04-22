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
# How many Mondays fell on the first of the month
# during the range (1 Jan 1 to 31 Dec 9999)?
# Solution:
# I will use datetime module and generator magic

from datetime import datetime

MONDAY = 0

count = sum(1 for date in (
    datetime(year, month, 1)
    for year in range(1, 10000)
    for month in range(1, 13))
    if date.weekday() == MONDAY)

print('There are {0} Mondays from 1/1/1 12/31/9999 '
      'on first day of month'.format(count))
