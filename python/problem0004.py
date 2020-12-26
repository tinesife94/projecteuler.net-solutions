def is_palindrome(key):
    '''Checks whether a string or number is palindrome.'''
    s = str(key)
    return s == s[::-1]

def largest_palindrome_product_of_2_3_digit_numbers():
    '''Returns the largest palindrome product made from the product of two
    3-digit numbers.'''
    ret = 0;
    aux = 0;
    for i in range(990, 99, -11):
        for j in range(999, i - 1, -1):
            if is_palindrome(i * j):
                aux = i * j;
                if aux > ret:
                    ret = aux
                elif ret - aux > 100000: 
                    # Probably won't find a bigger one from now on, so:
                    return ret
    return ret

print(largest_palindrome_product_of_2_3_digit_numbers())
