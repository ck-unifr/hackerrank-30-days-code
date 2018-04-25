# https://www.hackerrank.com/challenges/30-bitwise-and/problem

# Task
# Given set S = {1, 2, 3, ..., N} .
# Find two integers, A and B (where A < B), from set S such that the value of A&B  is the maximum possible
# and also less than a given integer K . In this case, & represents the bitwise AND operator.


#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n), int(k)]

    s = [i for i in range(1, n+1)]
    max_b = 0
    for i in range(len(s)-1):
        j = i+1
        while j < len(s):
            b = (i+1) & (j+1)
            if b < k and b > max_b:
                max_b = b
            j += 1

    print(max_b)

