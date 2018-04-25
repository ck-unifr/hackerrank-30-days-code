#https://www.hackerrank.com/challenges/30-regex-patterns/problem

# Task
# Consider a database table, Emails, which has the attributes First Name and Email ID.
# Given N rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email
# address ends in @gmail.com.

#!/bin/python3

import sys
import re

regex = re.compile("^[a-z\.]+@gmail.com$")
accounts = dict()

N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if regex.match(emailID):
        accounts[emailID] = firstName


sorted_names = sorted(accounts.values())
print(*sorted_names, sep="\n")