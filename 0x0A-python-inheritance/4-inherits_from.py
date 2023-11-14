#!/usr/bin/python3

'''4. sub class'''


def inherits_from(obj, a_class):
    '''function that shows if the object is an instance of
    a class that is inherited from the
    specified class.'''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
