#!/usr/bin/python3

"""This module creates a json file using
the __dict__ method of the obj
"""


def class_to_json(obj):
    """This returns a serializable list of all objects
    in obj

    Args:
        obj: the objects
    """
    return obj.__dict__
