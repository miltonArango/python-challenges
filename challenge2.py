"""
Challenge 2:

Read four integers, X, Y, Z, N

Where X, Y, and Z, represent the dimensions of a cuboid,
i,e,. The first dimension ranges from 0 to X, the second from 0 to Y,
and the third from 0 to Z

And print all the possible coordinates (i, j, k)
where the sum of i+j+k is different than N


Sample Input

As explained in the description.
E.g.:
X=1, Y=1, Z=1, N=2

Sample Output

Print the coordinates that satisfies the condition described above.
E.g.:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Test Case:

>>> get_coordinates(1, 1, 1, 2)
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""


def get_coordinates(X, Y, Z, n):
    """Return the coordinates [x, y, z] where x + y + z != n
       given X, Y, Z > 0.

    The specified dimensions have 27 (3 x 3 x 3) possible combinations
    So, the only coordinate different than 0 is the origin [0, 0, 0]
    Thus, the coordinates should be 26.
    >>> len(get_coordinates(2, 2, 2, 0))
    26

    The specified dimensions have 36 (4 x 3 x 3) possible combinations
    So, the only coordinate different than 0 is the origin [0, 0, 0]
    Thus, the coordinates should be 35.
    >>> len(get_coordinates(3, 2, 2, 0))
    35

    >>> get_coordinates(0, 1, 1, 0)
    Traceback (most recent call last):
        ...
    ValueError: Dimension must be > 0

    >>> get_coordinates(1.1, 1, 1, 0)
    Traceback (most recent call last):
        ...
    ValueError: Dimension must be an exact integer

    It must also not be ridiculously large:
    >>> get_coordinates(1e100, 1, 1, 0)
    Traceback (most recent call last):
        ...
    OverflowError: Dimension is too large
    """
    import math

    if not (X and Y and Z > 0):
        raise ValueError("Dimension must be > 0")
    if math.floor(X) != X or math.floor(Y) != Y or math.floor(Z) != Z:
        raise ValueError("Dimension must be an exact integer")
    if X + 1 == X or Y + 1 == Y or Z + 1 == Z:  # Catch a value like 1e300
        raise OverflowError("Dimension is too large")

    positions_list = []

    for x in range(X + 1):
        for y in range(Y + 1):
            for z in range(Z + 1):
                if sum((x, y, z)) != n:
                    positions_list.append(list((x, y, z)))
    return positions_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
