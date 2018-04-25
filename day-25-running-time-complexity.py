# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

# Task
# A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# Given a number n, determine and print whether it's  Prime or Not prime.



def is_prime(n):
    if n == 1:
        return False
    divisor = 2
    while divisor <= n**0.5:
        if n % divisor == 0:
            return False
        divisor += 1

    return True



T=int(input())
for i in range(T):
    n=int(input())
    if is_prime(n):
        print('Prime')
    else:
        print('Not prime')