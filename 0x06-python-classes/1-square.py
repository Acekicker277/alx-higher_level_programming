#!/usr/bin/python3
"""Class called square"""


class Square:
    """A class with private instance attribute 'size'"""
    __size = ''

    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
