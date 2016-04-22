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
# Multiply alphabetical value for each name to position in sorted list

# Solution:
# Straightforward

import os
from os.path import expanduser

home = expanduser("~")
os.chdir('%s/Downloads' % home)

# read data from text
with open('names.txt', 'r') as names:
    names = [name for name in names.read().split(',')]

# sort it
names.sort()


def alpha_value(name):
    ''' Value of each letter
    '''
    return sum(ord(letter) - ord('A') for letter in name if letter != '"')


print('Sum of values for each name is %s' % sum(
    (i * alpha_value(name)) for i, name in enumerate(names)))
