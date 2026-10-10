#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculates the factorial of a given non-negative integer recursively.

    Parameters:
        n (int): The non-negative integer whose factorial is to be computed.

    Returns:
        int: The computed factorial value (n!).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
