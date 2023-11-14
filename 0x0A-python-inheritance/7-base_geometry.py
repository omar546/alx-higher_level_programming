#!/usr/bin/python3

'''7. Integer validation'''


class BaseGeometry():
    '''class BaseGeometry'''

    def area(self):
        '''Function to raise an Exception with the message area()
        is not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''value validation:
        if value is less or equal to 0:
        raise a ValueError exception with the message
        if value is not an integer: raise a TypeError exception
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
