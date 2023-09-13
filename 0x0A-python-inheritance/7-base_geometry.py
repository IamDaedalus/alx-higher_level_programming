#!/usr/bin/python3

"""Another empty class to build on"""

class BaseGeometry:
    """This is the base class in the module or script
    """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")


    def area(self):
        """Raises an error to point out area is
        implemented yet
        """
        raise Exception("area() is not implemented")

