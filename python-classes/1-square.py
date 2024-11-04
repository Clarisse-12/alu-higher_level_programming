#!/usr/bin/python3
class Square:
    """
    This class defines a square with a private size attribute
    """
    def __init__(self, size):
        """
        Initialize the square
        Args:
            size: size of the square's side
        """
        self.__size = size
