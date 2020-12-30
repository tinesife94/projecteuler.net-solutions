def sum_AP(a1, an, n):
    '''Sum of n terms of the arithmetic progression.'''
    return ((a1 + an) * n) // 2

def sum_of_natural_numbers(n):
    '''Sum of the first n natural numbers.'''
    return sum_AP(1, n, n)

def sum_of_odd_numbers(n):
    '''Sum of the first n odd numbers.'''
    last = (2 * n) - 1
    return sum_AP(1, last, n)

def sum_of_the_squares(n):
    '''Sum of the squares of the first n natural numbers.'''
    return (n * ((2 * n) + 1) * (n + 1)) // 6

n = 100
result = sum_of_natural_numbers(n)
result **= 2
result -= sum_of_the_squares(n)

print(result)
