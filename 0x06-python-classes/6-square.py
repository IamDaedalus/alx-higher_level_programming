#!/usr/bin/python3

"""This class contains methods and attributes for
a creating a square, getting various properties about
it such as its position, size and area packaged in
a neat format
"""


class Square:
    """This class defines a square with private instance attribute 'size'"""
    def __init__(self, size=0, position=(0, 0)):
        """This method initialises a new class Square
        with private attribute size

        Args:
            size: the size of the Sqr as an int
            position: the position of the Sqr in vector
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter method to retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position of the
        square
        Args:
            value: the coordinate as tuple aka a vector
        """
        if not isinstance(value, tuple):
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError(
                    "position must be a tuple of 2 positive integers")

    def my_print(self):
        """Prints the square using '#' characters"""
        if self.__size == 0:
            print()
        else:
            for _ in range(0, self.__size):
                if self.position[0] > 0:
                    print(" " * self.position[0], end="")
                print("#" * self.__size)
