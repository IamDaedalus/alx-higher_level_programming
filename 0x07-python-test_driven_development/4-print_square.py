#!/usr/bin/python3

"""This module prints a square using #"""


def print_square(size):
    """This function prints a square of size
    size. size is converted to an integer otherwise the
    function raises an error.

    Args:
        size: the size of the square to print
    """
    if not isinstance(size, (int, float))\
            or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)

    if size == 1:
        print("#")
    else:
        for _ in range(int(size)):
            for _ in range(int(size) - 1):
                print("#", end="")
            print("#")
