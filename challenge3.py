"""
Challenge 3:

Read a string representing a sentence.
Convert all the spaces in this string to hyphens and print the output
Resolve this in just one line

Sample Input
hello world I am programming in Python

Output Format
hello-world-I-am-programming-in-Python

Test Case:

>>> replace_spaces('hello world I am programming in Python')
'hello-world-I-am-programming-in-Python'
"""


def replace_spaces(sentence):
    """Replaces whitespaces with hiphens in the given sentence

    >>> replace_spaces('test  test   test    ')
    'test--test---test----'

    >>> replace_spaces('')
    ''

    >>> replace_spaces(' ')
    '-'

    >>> replace_spaces('    test    ')
    '----test----'
    """
    return sentence.replace(' ', '-')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
