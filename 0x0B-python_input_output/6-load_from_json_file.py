#!/usr/bin/python3

"""This module contains a function to load json
data for us
"""

import json


def load_from_json_file(filename):
    """This function loads json data from a file

    Args:
        filename: the file name to load from
    """
    with open(filename, "r") as file:
        json.load(file)
