# https://www.hackerrank.com/challenges/30-binary-numbers/problem

# Task
# Given a base-10 integer, n, convert it to binary (base-2).
# Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

#!/bin/python3

import sys
import string
digs = string.digits + string.ascii_letters

n = int(input().strip())

def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

str_int_2 = int2base(n, 2)

max_n_1 = 0

for i in range(0, len(str_int_2)-1):
    n_1 = 0
    loop = True
    j = i
    while loop and j < len(str_int_2):
        if str_int_2[j] == '1':
            n_1 += 1
        else:
            loop = False
        j += 1

    if n_1 > max_n_1:
        max_n_1 = n_1

print(max_n_1)