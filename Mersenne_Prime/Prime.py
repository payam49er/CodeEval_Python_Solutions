__author__ = 'payam'

import sys

primes = [3, 7, 31, 127, 2047]

def __GenerateMersenne(number):
    numbers = []
    for x in primes:
        if number > x:
            numbers.append(x)
    print ", ".join(str(s) for s in numbers)


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        __GenerateMersenne(int(test, 10))







