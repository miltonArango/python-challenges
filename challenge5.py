"""
Challenge 5:

Compute the classroom marks average
Read an integer representing the total count of students (N)
Read a string representing the columns of the students,
they can be in any order
Read N lines for each student records with the same columns as above

Sample input
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

Sample output
78.00

Sample input
5
MARKS      CLASS      NAME       ID
92         2          Calum      1
82         5          Scott      2
94         2          Jason      3
55         8          Glenn      4
82         2          Fergus     5

Sample output
81.00

Restrictions:
* You are not allowed to use external libraries, only core python ones.
* Target for different inputs with different column order.
(Notice in the samples above, both have different column order),
Your solution should work no matter if different inputs works.

Extra marks:
* Try to solve in 4 lines or less, but a correct solution in more than 4
lines is valid too.

Hints:
* Named Tuples
"""


def compute_class_averages(n, cols):
    """Returns the class marks average computed from the input column string

    >>> sample1 = '''
    ...     ID      CLASS           NAME       MARKS
    ...     1         2          Calum      70
    ...     2         5          Scott      59
    ...     3         2          Jason      66
    ...     4         8          Glenn      98
    ...     5         2          Fergus     89
    ...     '''
    >>> compute_class_averages(5, sample1)
    76.4

    >>> sample2 = '''
    ...     ID         MARKS      NAME       CLASS
    ...     1          97         Raymond    7
    ...     2          50         Steven     4
    ...     3          91         Adrian     9
    ...     4          72         Stewart    5
    ...     5          80         Peter      6
    ...     '''
    >>> compute_class_averages(5, sample2)
    78.0

    >>> sample3 = '''
    ...     MARKS      CLASS      NAME       ID
    ...     92         2          Calum      1
    ...     82         5          Scott      2
    ...     94         2          Jason      3
    ...     55         8          Glenn      4
    ...     82         2          Fergus     5
    ...     '''
    >>> compute_class_averages(5, sample3)
    81.0
    """

    marks = cols.split('\n')[1].split().index('MARKS')
    grades = [int(x.split()[marks]) for x in cols.split('\n')[2:-1]]
    return float(sum(grades)) / len(grades)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
