#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute for size.
The Square class represents a square shape with a specified size attribute,
which is kept private to ensure controlled access and modification.
"""


class Square:
    """
    Class that defines a square with a private instance attribute for size.

    The size of a square is kept private to allow controlled access in the
    future, as the size attribute will be important for calculations such as
    area and perimeter.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a private size attribute.

        Args:
            size: The size of one side of the square.

        This size attribute is private to ensure controlled access and
        modification, which will be crucial for size-dependent calculations.
        """
        self.__size = size
