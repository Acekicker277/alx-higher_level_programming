#!/usr/bin/python3
"""Class called square"""


class Square:
    """A class with private instance attribute 'size'"""
    __size = ''

    def __init__(self, size=0):
        """Instantiation with size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """A public instance method that returns the current square area """
        return self.__size * self.__size
