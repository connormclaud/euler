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
# Decrypt message

# Solution:
# Frequency analisys.
from collections import Counter
from itertools import cycle


def read_file(filename='p059_cipher.txt'):
    with open(filename, 'r') as f:
        content = f.read()
    encrypted_letters = content[:-1].split(',')
    return encrypted_letters


def split_for_each_key(cypher):
    ''' We know that key is 3 symbols long '''
    return cypher[::3], cypher[1::3], cypher[2::3]


def key_from_frequency(counter):
    ''' We assume that space is most frequent character '''
    return chr(int(counter[0][0]) ^ ord(' '))


def find_key(cypher):
    cyphers = split_for_each_key(cypher)
    counters = [Counter(item).most_common(1) for item in cyphers]
    key = "".join(key_from_frequency(counter) for counter in counters)
    return key


def decrypt(cypher, key):
    return "".join(chr(int(i) ^ ord(j)) for i, j in zip(cypher, cycle(key)))


def find():
    cypher = read_file()
    key = find_key(cypher)
    print('Key is "%s"' % key)
    original_text = decrypt(cypher, key)
    print(original_text)
    return sum(ord(letter) for letter in original_text)


find()
