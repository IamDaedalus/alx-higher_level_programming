#!/usr/bin/python3

"""This module checks if an obj inherits
from a class
"""


def inherits_from(obj, a_class):
    """This compares if they inherit the same
    base class

    Args:
        obj: the obj to compare
        a_class: the class to compare with
    """
    return not issubclass(a_class, type(obj))
