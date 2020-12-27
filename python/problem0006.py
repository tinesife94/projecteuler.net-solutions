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

n = 100
result = sum_of_natural_numbers(n)
result = sum_of_odd_numbers(result)

for i in range(1, n + 1):
    result -= sum_of_odd_numbers(i)

print(result)
