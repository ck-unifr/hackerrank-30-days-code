# https://www.hackerrank.com/challenges/30-loops/problem

#!/bin/python3

import sys


n = int(input().strip())

for i in range(10):
    print('{} x {} = {}'.format(str(n), str(i+1), str(n*(i+1))))
