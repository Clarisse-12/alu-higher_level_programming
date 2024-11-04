#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute for size.
The Square class represents a square shape with a specified size attribute.
The size is validated to be a non-negative integer, and an area method
is provided.
"""


class Square:
    """
    Class that defines a square with a private instance attribute for size.

    The size of a square is kept private to allow controlled access and
    modification, and is validated to be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with a private size attribute.

        Args:
            size (int): The size of one side of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square, calculated as size * size.
        """
        return self.__size * self.__size
