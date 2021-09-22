'''
Calculate the factorial of a number using a recursive function.
'''


def fact(n):
    '''
    Returns factorial of n (n!).
    Note use of recursion
    '''
    # BASE CASE!
    if n == 0:
        return 1
    # Recursion!
    else:
        return n * fact(n - 1)


print(fact(5))
