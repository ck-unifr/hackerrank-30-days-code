# https://www.hackerrank.com/challenges/30-sorting/problem


# Task
# Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above.
# Once sorted, print the following  lines:
#
# Array is sorted in numSwaps swaps.
# where  numSwaps is the number of swaps that took place.

# First Element: firstElement
# where firstElement is the first element in the sorted array.

# Last Element: lastElement
# where lastElement is the last element in the sorted array.

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

totalNumSwaps = 0
for i in range(0, len(a)):
    numSwaps = 0
    for j in range(0, len(a)-1):
        if(a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numSwaps += 1
    totalNumSwaps += numSwaps

    if numSwaps == 0:
        break

print('Array is sorted in {} swaps.'.format(totalNumSwaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))

