# https://www.hackerrank.com/challenges/30-interfaces/problem

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        """
        return the sum of all divisors of n
        """
        sum_divisor = 0
        for i in range(1, n+1):
            if n % i == 0:
                sum_divisor += i
        return sum_divisor