#!/usr/bin/python3
"""
Copyright (C) 2021

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import re
import array

from mathlib_TTT import MathlibTTT


def main():
    numbers = []
    for line in sys.stdin:
        if line == '':
            break
        strings = re.split(' |\t', line)
        for n in strings:
            n = n.replace('\n', '')
            if n.isnumeric():
                numbers.append(int(n))

    N = len(numbers)
    if N == 0:
        return 0;

    sum = 0
    for n in numbers:
        sum = MathlibTTT.add(sum, n)

    x = MathlibTTT.div(sum, N)

    Nxsquared = MathlibTTT.mul(N, MathlibTTT.pow(x, 2))
    temp = 0
    for n in numbers:
        xsquared = MathlibTTT.pow(n, 2)
        temp = MathlibTTT.add(temp, xsquared)

    temp = MathlibTTT.sub(temp, Nxsquared)

    s = MathlibTTT.root(MathlibTTT.div(temp, MathlibTTT.sub(N, 1)), 2)
    print(str(s))
    return 0


if __name__ == '__main__':
    sys.exit(main())
