# https://www.hackerrank.com/challenges/30-arrays/problem

# Task
# Given an array,A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.


#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr = arr[::-1]

str_arr = ''
for a in arr:
    str_arr += str(a) + ' '
print(str_arr)