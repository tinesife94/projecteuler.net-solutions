"""Python code to solve problem 3 on the projecteuler.net website, available
at:

https://projecteuler.net/problem=3

For your convinience:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math

def p_largest_prime_factor(num : int, start : int, largest : int) -> int:
    """Find the largest prime factor of an odd number"""
    if largest * largest > num:
        return num
    lim = int(math.sqrt(num)) + 1
    for i in range(start, lim, 2):
        if num % i == 0:
            largest = i
            while num % i == 0:
                num //= i
                if num == 1:
                    return largest
            return p_largest_prime_factor(num, i + 2, largest)
    return num

def largest_prime_factor(num : int) -> int:
    """Find the largest prime factor of any number"""
    largest = 1
    if num % 2 == 0:
        largest = 2
        while num % 2 == 0:
            num //= 2
            if num < 4:
                return max(2,num)
    return p_largest_prime_factor(num, 3, largest)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(largest_prime_factor(600_851_475_143))
    elif len(sys.argv) == 2:
        print(largest_prime_factor(int(sys.argv[1])))
