#!/usr/bin/python3

"""Module for creating a square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class to create a new square that inherits
    from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the square class

        Args:
            size: the size of the square
            x: the x position of the square
            y: the y position of the square
            id: the instance id of the square
        """
        super().__init__(size, size, x, y, id)

    # GETTERS AND SETTERS BEGIN
    @property
    def size(self):
        """Getter method for the Square"""
        return super().width

    @size.setter
    def size(self, value):
        """Setter method for the Square"""
        self.width = value
        self.height = value
    # GETTERS AND SETTERS END

    def update(self, *args, **kwargs):
        """This method updates attributes based on *args or **kwargs

        Args:
            args: Variable-length positional arguments
            kwargs: Variable-length keyword arguments
        """
        attributes = ['id', 'width', 'height', 'x', 'y']

        if args:
            if len(args) > 4:
                raise IndexError("Too many positional arguments")
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
        else:
            raise ValueError("No arguments provided")

    def __str__(self):
        """This method returns the string representation of
        a Square instance
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.x, self.x, self.y, self.height)
