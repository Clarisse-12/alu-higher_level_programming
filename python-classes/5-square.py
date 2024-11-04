#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute for size.
The Square class represents a square shape with size validation, a getter and
setter for size, a method to calculate area, and a method to print the square.
"""


class Square:
    """
    Class that defines a square with a private instance attribute for size.

    The size of a square is kept private to ensure controlled access and
    modification. The class includes a getter and setter for size to handle
    validation in one place, following object-oriented principles.
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
        self.size = size  # Uses the property setter for validation

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of one side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The size to set for one side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square, calculated as size * size.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character #.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
