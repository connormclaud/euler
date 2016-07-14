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
# Poker hand evaluation
# Solution:

from collections import Counter
from itertools import groupby, compress
from operator import itemgetter
from functools import total_ordering


@total_ordering
class Hand():
    rank = (
        '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
    ranking = {value: index for index, value in enumerate(rank)}
    combinations = [
        'High Card',
        'One Pair',
        'Two Pairs',
        'Three of a Kind',
        'Straight',
        'Flush',
        'Full House',
        'Four of a Kind',
        'Straight Flush',
        'Royal Flush']

    combirank = {value: index for index, value in enumerate(combinations)}

    def __init__(self, cards):
        self.cards = list(cards)
        self.sorted_hand = sorted(ranking[card[0]] for card in cards)
        self.counter = [
            (rank, count) for rank, count
            in Counter(ranking[card[0]] for card in self.cards).most_common(2)
            if count > 1]
        self.higher_cards = ([i for i in reversed(self.sorted_hand)
                              if i not in {
            rank[0] for rank in self.counter}])

    def is_straight(self):
        group = groupby(enumerate(self.sorted_hand), lambda i: i[1] - i[0])
        return next(group, True) and not next(group, False)

    def is_flush(self):
        seen = set(card[1] for card in self.cards)
        return len(seen) == 1

    def is_full_house(self):
        return (len(self.counter) == 2 and self.counter[0][1] == 3
                and self.counter[1][1] == 2)

    def is_three_of_kind(self):
        return len(self.counter) == 1 and self.counter[0][1] == 3

    def is_two_pairs(self):
        return (len(self.counter) == 2 and self.counter[0][1] == 2
                and self.counter[1][1] == 2)

    def is_pair(self):
        return len(self.counter) == 1 and self.counter[0][1] == 2

    def _highest_rank(self):
        return self.sorted_hand[-1]

    def is_royal_flush(self):
        return (self.is_straight_flush()
                and self._highest_rank() == self.ranking['A'])

    def is_straight_flush(self):
        return self.is_straight() and self.is_flush()

    def is_four_of_kind(self):
        return (max(self.counter, key=itemgetter(1), default=(0,0)))[1] == 4

    def __eq__(self, other):
        if not self.combination_rank() == other.combination_rank():
            return False

        for mine, theirs  in zip(
                self.combination_power(), other.combination_power()):
            if mine != theirs:
                return False

        for mine, theirs in zip(self.other_ranks(), other.other_ranks()):
            if mine != theirs:
                return False
        return True

    def __lt__(self, other):
        if self.combination_rank() == other.combination_rank():
            for mine, theirs  in zip(
                self.combination_power(), other.combination_power()):
                if mine == theirs:
                    continue
                return mine < theirs
            for mine, theirs in zip(self.other_ranks(), other.other_ranks()):
                if mine == theirs:
                    continue
                return mine < theirs
        else:
            return self.combination_rank() < other.combination_rank()

        return False

    def combination_power(self):
        return (i[0] for i in self.counter)

    def other_ranks(self):
        return (i for i in self.higher_cards)

    def combination(self):
        checks = [
            False,
            self.is_pair(),
            self.is_two_pairs(),
            self.is_three_of_kind(),
            self.is_straight(),
            self.is_flush(),
            self.is_full_house(),
            self.is_four_of_kind(),
            self.is_straight_flush(),
            self.is_royal_flush()]

        result = list(compress(self.combinations, checks))
        result = self.combinations[0] if not result else result[-1]
        return result

    def combination_rank(self):
        return self.combirank.get(self.combination(), None)

    def __str__(self):
        return 'Hand: %s' % str(self.cards)

    def __repr__(self):
        return 'Hand(%s)' % self.cards


def find():
    return sum(1 for hand1, hand2 in hands_from_file() if hand1 < hand2)

def hands_from_file(filename='p054_poker.txt'):
    with open(filename, 'r') as f:
        for line in f:
            hands = line.split()
            player1_hand = Hand(hands[:5])
            player2_hand = Hand(hands[5:])
            yield player1_hand, player2_hand

print('Player 2 wins %s times' % find())
