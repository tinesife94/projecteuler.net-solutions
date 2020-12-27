import math

def prime_number_candidates(n):
    '''Returns a good list of prime number candidates.'''
    if n >= 2:
        possible = [2, 3]
        return get_more_candidates(possible, n - 2)
    elif n == 1:
        return [2]

def get_more_candidates(candidates, n):
    '''Insufficient candidates, add more.'''
    for i in range(n):
        if candidates[-1] % 6 == 1:
            candidates.append(candidates[-1] + 4)
        else:
            candidates.append(candidates[-1] + 2)
    return candidates

def prime_numbers(n):
    '''Find the first n prime numbers'''
    primes = []
    possibles = prime_number_candidates(n)
    m_i = -1;
    while True:
        for i in range(m_i + 1, len(possibles)):
            m_i = max(i, m_i)
            lim = int(math.sqrt(possibles[i]))
            for j in range(i):
                if possibles[j] > lim:
                    primes.append(possibles[i])
                    if (len(primes) == n):
                        return primes
                    break;
                if possibles[i] % possibles[j] == 0:
                    break;
            else:
                primes.append(possibles[i])
                if (len(primes) == n):
                    return primes
        possibles = get_more_candidates(possibles, n)

def get_the_nth_prime_number(n):
    '''Get a specific prime number.'''
    return prime_numbers(n)[-1]

print(get_the_nth_prime_number(10001))
