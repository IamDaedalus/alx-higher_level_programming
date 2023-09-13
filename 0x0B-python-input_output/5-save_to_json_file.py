#!/usr/bin/python3

"""This module contains a function that writes
json representation of an obj to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """The function to write a json representation of
    an object to file naemd filename

    Args:
        my_obj: the obj
        filename: the filename
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
