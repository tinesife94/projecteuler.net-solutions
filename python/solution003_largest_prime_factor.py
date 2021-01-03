"""Python code to solve problem 3 on the projecteuler.net website, available
at:

https://projecteuler.net/problem=3

For your convinience:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math

def p_largest_prime_factor(num, start=3, largest=1):
    '''Find the largest prime factor of an odd number'''
    if largest * largest > num:
        return num
    lim = int(math.sqrt(num)) + 1
    for i in range(start, lim, 2):
        if num % i == 0:
            largest = i
            while num % i == 0:
                num //= i
            return p_largest_prime_factor(num, i + 2, largest)
    return num

def largest_prime_factor(num):
    '''Find the largest prime factor of any number'''
    largest = 1
    if num % 2 == 0:
        largest = 2
        while num % 2 == 0:
            num //= 2
            if num < 4:
                return max(2,num)
    return p_largest_prime_factor(num, 3, largest)

print(largest_prime_factor(600851475143))
