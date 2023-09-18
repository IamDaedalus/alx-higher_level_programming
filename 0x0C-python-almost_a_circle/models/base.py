#!/usr/bin/python3

"""Base class for the incoming tasks
"""

from collections.abc import Iterator
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
        if id is not None and type(id) is int:
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
        """Writes the JSON representation of a list of instances
        of this class to a file named <class-name>.json

        Args:
            list_objs: a list of objects that inherit from this
        """
        filename = cls.__name__ + ".json"
        items = []
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                for obj in list_objs:
                    items.append(obj.to_dictionary())
                file.write(cls.to_json_string(items))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of json string representation

        Args:
            json_string: the str
        """
        if json_string is None or not isinstance(json_string, str):
            return '[]'
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        pass