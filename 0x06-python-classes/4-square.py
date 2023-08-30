#!/usr/bin/python3

"""This is an empty class that will be built upon
to help create a new Square object to used in our program.

As time goes on we'll expand on it's methods and fields so
that over time it becomes more and more useful
"""

class Square:
    """This class defines a square with private instance attribute 'size'"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size

            Args:
                value: the value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
