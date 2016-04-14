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
# If all the numbers from 1 to 1000000 (one million) inclusive
# were written out in words, how many letters would be used?

# Solution:
# convert all numbers to text
# I use algorithm described in
# http://www.blackwasp.co.uk/NumberToWords.aspx

# Single-digit and small number names
_small_numbers = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six',
    'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen',
    'eighteen', 'nineteen']

# tens number names from twenty upwards
_tens_numbers = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty',
    'sixty', 'seventy', 'eighty', 'ninety']

# Scale number names for use during recombination
_scale_numbers = ['', 'thousand', 'million', 'billion']


def group_to_text(group):
    text = ''
    hundreds = group / 100
    tens_unit = group % 100

    if hundreds != 0:
        text += _small_numbers[hundreds] + ' hundred'
        if tens_unit != 0:
            text += ' and '

    tens = tens_unit / 10
    units = tens_unit % 10

    if tens >= 2:
        text += _tens_numbers[tens]
        if units != 0:
            text += ' ' + _small_numbers[units]
    elif tens_unit != 0:
        text += _small_numbers[tens_unit]

    return text


def number_to_word(number):
    if number == 0:
        return _small_numbers[0]
    digit_groups = []
    positive = abs(number)
    for i in _scale_numbers:
        digit_groups.append(positive % 1000)
        positive //= 1000

    group_text = []
    for group in digit_groups:
        group_text.append(group_to_text(group))

    text = group_text[0]
    and_needed = 0 < digit_groups[0] < 100

    for item, group in enumerate(group_text[1:], 1):
        if digit_groups[item] != 0:
            prefix = group + ' ' + _scale_numbers[item]
            if len(text) and and_needed:
                prefix += ' and'
            and_needed = False
            text = prefix + ' ' + text

    return text

def count_letters(word):
    ''' count letters besides spaces
    '''
    return len([letter for letter in word if letter not in (' ')])

number_of_letters = sum(
    count_letters(number_to_word(i)) for i in xrange(1, 1000001))
#
print ('Number of letters in numbers from '
       '1 to 1000000 written in words is %s ' % number_of_letters)
