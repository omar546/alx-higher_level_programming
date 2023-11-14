#!/usr/bin/python3

'''11. Square two'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square'''

    def __init__(self, size):
        '''Init atributes'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        '''Def __str__ Method'''
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
