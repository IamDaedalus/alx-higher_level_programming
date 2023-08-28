#!/usr/bin/python3

def no_c(my_string):
    """Removes all occurences of c from the string\n
    my_string

    Args:
        my_string: the string to operate on
    """
    new_str = ""

    for i in range(0, len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_str += my_string[i]

    return new_str


