def even_fib(lim):
    '''Get the even terms of the Fibonacci sequence (less than lim).'''
    terms = []
    a, b = 0, 1
    while (a < lim):
        if a % 2 == 0:
            terms.append(a)
        a, b = b, a + b
    return terms

print(sum(even_fib(4000000)))
