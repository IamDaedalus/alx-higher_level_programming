#!/usr/bin/python3

"""This class contains methods and attributes for
a creating a square, getting various properties about
it such as its position, size and area packaged in
a neat format
"""


class Square:
    """This class defines a square with private instance attribute 'size'"""
    def __init__(self, size=0):
        """This method initialises a new class Square
        with private attribute size

        Args:
            size: the size of the Sqr as an int
        """
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
