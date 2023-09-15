#!/usr/bin/python3

"""Base class for the incoming tasks
"""


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
