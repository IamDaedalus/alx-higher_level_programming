#!/usr/bin/python3

"""Another empty class to build on"""


class BaseGeometry:
    """This is the base class in the module or script
    """
    def integer_validator(self, name, value):
        """This function validates the value paramater

        Args:
            name: a string
            value: value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """Raises an error to point out area is
        implemented yet
        """
        raise Exception("area() is not implemented")
