"""Python code to solve problem 5 on the projecteuler.net website, available
at:

https://projecteuler.net/problem=5

For your convinience:

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

elements = []

for i in range(2,20):
    for v in elements:
        q, r = divmod(i, v)
        if not r:
            i = q
            if i == 1:
                break
    else:
        elements.append(i)

mul = 1
for v in elements:
    mul *= v

print(mul)
