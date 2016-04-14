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
# Find the maximum total from top to bottom of the triangle below:

# Solution:
# It is possible to solve this using shortest paths in directed acyclic graphs
# in linear time, but I like more dynamic programming approach when we go
# from bottom to top and eliminate all impossible paths

# data structure: Here 2d array  is enough. We imply graph with implicit edges

input = '''
59
73 41
52 40 09
26 53 06 34
10 51 87 86 81
61 95 66 57 25 68
90 81 80 38 92 67 73
30 28 51 76 81 18 75 44
84 14 95 87 62 81 17 78 58
21 46 71 58 02 79 62 39 31 09
56 34 35 53 78 31 81 18 90 93 15
78 53 04 21 84 93 32 13 97 11 37 51
45 03 81 79 05 18 78 86 13 30 63 99 95
39 87 96 28 03 38 42 17 82 87 58 07 22 57
06 17 51 17 07 93 09 07 75 97 95 78 87 08 53
67 66 59 60 88 99 94 65 55 77 55 34 27 53 78 28
76 40 41 04 87 16 09 42 75 69 23 97 30 60 10 79 87
12 10 44 26 21 36 32 84 98 60 13 12 36 16 63 31 91 35
70 39 06 05 55 27 38 48 28 22 34 35 62 62 15 14 94 89 86
66 56 68 84 96 21 34 34 34 81 62 40 65 54 62 05 98 03 02 60
38 89 46 37 99 54 34 53 36 14 70 26 02 90 45 13 31 61 83 73 47
36 10 63 96 60 49 41 05 37 42 14 58 84 93 96 17 09 43 05 43 06 59
66 57 87 57 61 28 37 51 84 73 79 15 39 95 88 87 43 39 11 86 77 74 18
54 42 05 79 30 49 99 73 46 37 50 02 45 09 54 52 27 95 27 65 19 45 26 45
71 39 17 78 76 29 52 90 18 99 78 19 35 62 71 19 23 65 93 85 49 33 75 09 02
33 24 47 61 60 55 32 88 57 55 91 54 46 57 07 77 98 52 80 99 24 25 46 78 79 05
92 09 13 55 10 67 26 78 76 82 63 49 51 31 24 68 05 57 07 54 69 21 67 43 17 63 12
'''

data = []
for line in input[1:].splitlines():
    data.append([int(s) for s in line.split()])

# go bottom to top

reverse = data[::-1]
while len(reverse) > 1:
    for i, lst in enumerate(reverse[1:2], 1):
        for position, item in enumerate(lst):
            left = reverse[i - 1][position]
            right = reverse[i - 1][position + 1]
            # eliminate minimum path by merging
            reverse[i][position] = max(item + left, item + right)

    # make problem one line shorter
    del reverse[0]

print reverse[0][0]
#
