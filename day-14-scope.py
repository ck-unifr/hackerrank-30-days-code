# https://www.hackerrank.com/challenges/30-scope/problem
# Fork https://github.com/thechampanurag/hackerrank-30-Days-of-Code/blob/master/Day-14-scope.py

class Difference:

    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        a = self.__elements
        self.maximumDifference = max(a) - min(a)
# End of Difference class

a = [int(e) for e in "1 2 5".split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
