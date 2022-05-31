#!/usr/bin/python3
"""
This program create a Square from a Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Squared based from Rectangle"""

    def __init__(self, size):
        """Constructor of Square"""
        super().__init__(size, size)
        self.__size = size
