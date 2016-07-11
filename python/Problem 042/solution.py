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
# Find word with largest triangle value
# Solution:
# obvious

from itertools import takewhile

def triangle_generator():
    n = 0
    while True:
        yield n * (n + 1) // 2
        n += 1


def letter_position(letter):
    return ord(letter.upper()) - ord('A') + 1


def word_value(word):
    return sum(letter_position(letter) for letter in word.upper()
               if letter != '"')


def read_file(filename='p042_words.txt'):
    with open(filename, 'r') as f:
        content = f.read()

    return content.split(',')


def calculate_value():
    return {word: word_value(word) for word in read_file()}


def find():
    score = calculate_value()
    max_score = max(score.values())
    triangles = {item for item in takewhile(
        lambda x: x <= max_score, triangle_generator())}
    result = {key: score[key] for key in score if score[key] in triangles}
    return max(result, key=result.get)


print('Maximum triangle value has a word', find())
