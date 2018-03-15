# https://www.hackerrank.com/challenges/30-data-types/problem
import sys

# Declare second integer, double, and String variables.
i = 4
d = 4.0
s = 'HackerRank'

# Read and save an integer, double, and String to your variables.
var1 = int(input())
var2 = float(input())
var3 = input().strip()

# Print the sum of both integer variables on a new line.
print(i + var1)

# Print the sum of the double variables on a new line.
print(round(d + var2, 1))

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + ' ' + var3)
