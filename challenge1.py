"""
Challenge 1:

Read an integer N

Without using any string methods, try to print the following:

123...N

Test Case:

>>> print_array(5)
'12345'
"""


def print_array(n):
    """Print the value concatenation of an integer array of N elements
       given n >= 0.

    >>> [print_array(n) for n in range(1, 7)]
    ['1', '12', '123', '1234', '12345', '123456']
    >>> print_array(10)
    '12345678910'
    >>> print_array(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    >>> print_array(10.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer

    It must also not be ridiculously large:
    >>> print_array(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    from functools import reduce
    import math

    if not n >= 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return str(n)
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:  # Catch a value like 1e300
        raise OverflowError("n too large")

    return reduce(lambda x, y: str(x) + str(y), range(1, n + 1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
