"""Python code to solve problem 7 on the projecteuler.net website, available
at:

https://projecteuler.net/problem=7

For your convinience:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math

def prime_number_candidates(n):
    '''Returns a good list of prime number candidates.'''
    if n >= 2:
        possible = [2, 3]
        return get_more_candidates(possible, n - 2)
    if n == 1:
        return [2]
    return []

def get_more_candidates(candidates, n):
    '''Insufficient candidates, add more.'''
    for _ in range(n):
        if candidates[-1] % 6 == 1:
            candidates.append(candidates[-1] + 4)
        else:
            candidates.append(candidates[-1] + 2)
    return candidates

def prime_numbers(n):
    '''Find the first n prime numbers'''
    primes = []
    possibles = prime_number_candidates(n)
    m_i = -1
    while True:
        for i in range(m_i + 1, len(possibles)):
            m_i = max(i, m_i)
            lim = int(math.sqrt(possibles[i]))
            for j in range(2, i):
                if possibles[j] > lim:
                    primes.append(possibles[i])
                    if len(primes) == n:
                        return primes
                    break
                if possibles[i] % possibles[j] == 0:
                    break
            else:
                primes.append(possibles[i])
                if len(primes) == n:
                    return primes
        possibles = get_more_candidates(possibles, n)

def get_the_nth_prime_number(n):
    '''Get a specific prime number.'''
    return prime_numbers(n)[-1]

print(get_the_nth_prime_number(10_001))
