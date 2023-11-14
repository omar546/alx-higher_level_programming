#!/usr/bin/python3

'''10. Square one'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size):
        '''Init atributes'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
