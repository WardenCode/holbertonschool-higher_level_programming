#!/usr/bin/python3
"""
Create a Class Square with:
- size, position private propreties
- method of area and method of print_square
- getters & setters.
"""


class Square:
    """Class - Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor of a Square with the size and position"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

        if ((type(position) is not tuple) and (int not in position)):
            raise (TypeError("position must be a tuple of 2 positive integers"))
        else:
            self.__position = position
            
    def area(self):
        """Method to get the area of the Square"""
        return (self.__size ** 2)

    def my_print(self):
        """Method to print a Square with spaces"""
        max_on_tuple = max(self.position)
        if (self.__size == 0):
            print()
        else:
            for rows in range(self.__size):
                print(" " * max_on_tuple, end='')
                print("#" * self.__size)

    @property
    def size(self):
        """Getter of the private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for the size private attribute"""
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if ((type(value) is not tuple) and (int not in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
