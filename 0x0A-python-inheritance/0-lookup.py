#!/usr/bin/python3

"""
Module to return object's attributes and methods
"""


def lookup(obj):
    """This function returns a list of available
    attributes and methods of an object obj

    Args:
        obj: the object to returns its attributes
    """
    return dir(obj)
