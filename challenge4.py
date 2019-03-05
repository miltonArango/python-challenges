"""
Challenge 4:

Read a string with name and last name of a person,
ensure all the words of this string are capitalized.

Sample Input
pedro perez

Sample Output
Pedro Perez

Test Case:

>>> capitalize_name('pedro perez')
'Pedro Perez'
"""


def capitalize_name(name):
    """Capitalizes the given name

    >>> capitalize_name('pepito perez  rodriguez')
    'Pepito Perez Rodriguez'

    >>> capitalize_name('jorge Pérez lópez')
    'Jorge Pérez López'

    >>> capitalize_name('ramón valdez')
    'Ramón Valdez'
    """
    return ' '.join([s.capitalize() for s in name.split()])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
