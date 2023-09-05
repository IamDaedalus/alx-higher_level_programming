#!/usr/bin/python3

"""A simple module to add two integers together"""


def add_integer(a, b=98):
    """Add two numbers together as integers
    Args:
        a: the first value
        b: the second value
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
