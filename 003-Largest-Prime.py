# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def print_factors(x):
    """
    This takes the x value and
    """
    for n in range(1, int(math.sqrt(x))):
        if x % n == 0:
            if is_prime(n) is True:
                print(n)
            # print(isprime(factor))


def is_prime(x):
    prime = True
    for n in range(2, int(math.sqrt(x)) + 1):
        if x % n == 0:
            prime = False
    return prime

print_factors(600851475143)


""" Congratulations, the answer you gave to problem 3 is correct.

# You are the 321886th person to have solved this problem. """
