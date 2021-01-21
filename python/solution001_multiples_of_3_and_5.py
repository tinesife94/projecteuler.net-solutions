"""Python code to solve problem 1 on the projecteuler.net website, available
at:

https://projecteuler.net/problem=1

For your convinience:
----------------------------------------------------------------------------
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
----------------------------------------------------------------------------
Usage:

python solution001_multiples_of_3_and_5.py [multiples] [limit]

Examples:

python solution001_multiples_of_3_and_5.py 3 5 1000

python solution001_multiples_of_3_and_5.py 1000

python solution001_multiples_of_3_and_5.py 3 5

python solution001_multiples_of_3_and_5.py
"""

def sum_terms_arithmetic_progression(start: int, stop: int, step: int) -> int:
    """Sum of terms of an arithmetic progression.

    An efficient way to get the sum of all multiples of a number up to a
    certain stop.

    Sum of all multiples of 3 up to 10 (3 + 6 + 9):

    >>> sum_terms_arithmetic_progression(3, 10, 3)
    18
    """
    try:
        last = stop - stop % step
    except ZeroDivisionError:
        return start
    if stop == last:
        last -= step
    num_of_terms = ((last - start) // step) + 1
    return ((start + last) * num_of_terms) // 2

def sum_all_multiples_of_x_or_y_below_lim(x_value: int, y_value: int,
                                          lim: int) -> int:
    """Find the sum of all the multiples of x_value or y_value below lim.

    Sum of all multiples of 3 or 5 below 10 (3 + 5 + 6 + 9):

    >>> sum_all_multiples_of_x_or_y_below_lim(3, 5, 10)
    23
    """
    x_times_y = x_value * y_value
    return (sum_terms_arithmetic_progression(x_value, lim, x_value)
            + sum_terms_arithmetic_progression(y_value, lim, y_value)
            - sum_terms_arithmetic_progression(x_times_y, lim, x_times_y))

def _solution(argv : []) -> None:
    num_args = len(argv)
    if num_args == 3:
        x_arg, y_arg, lim_arg = argv
    elif num_args == 2:
        x_arg, y_arg, lim_arg = argv + [1_000]
    elif num_args == 1:
        x_arg, y_arg, lim_arg = 3, 5, argv[0]
    else:
        x_arg, y_arg, lim_arg = 3, 5, 1_000
    print(sum_all_multiples_of_x_or_y_below_lim(x_arg, y_arg, lim_arg))

if __name__ == "__main__":
    import sys
    import doctest
    doctest.testmod()
    _solution([int(num) for num in sys.argv if num.isdigit()])
