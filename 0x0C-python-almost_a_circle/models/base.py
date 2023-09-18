#!/usr/bin/python3

"""Base class for the incoming tasks
"""

import json


class Base:
    """The Base class; the progenitor; Adam himself!
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        Args:
            id: the id of the current instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This returns the json representation of the
        list of dictionaries

        Args:
            list_dictionaries: a list of dictionaries
        """
        if len(list_dictionaries) == 0 or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8"):
            for i in range(len(list_objs)):
                cls.to_json_string(list_objs[i])
