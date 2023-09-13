#!/usr/bin/python3

"""This module converts an obj into its json
representation
"""

import json


def to_json_string(my_obj):
    """This function converts an obj into json

    Args:
        my_obj: the object to convert
    """
    return json.dumps(my_obj)
