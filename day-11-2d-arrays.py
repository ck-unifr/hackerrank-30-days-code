# https://www.hackerrank.com/challenges/30-2d-arrays/problem

#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)


max_sum = -9 * 7

for i in range(0, len(arr)-2):
    for j in range(0, len(arr[i])-2):
        sum_h = 0
        sum_h += int(arr[i][j]) + int(arr[i][j+1]) + int(arr[i][j+2])
        sum_h += int(arr[i+1][j+1])
        sum_h += int(arr[i+2][j]) + int(arr[i+2][j + 1]) + int(arr[i+2][j + 2])
        if sum_h > max_sum:
            max_sum = sum_h

print(max_sum)

