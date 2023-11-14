#!/usr/bin/python3

'''3. exact class or inherited'''


def is_kind_of_class(obj, a_class):
    '''functionto show if the object is an instance
    a class or (inherited from),
    the specified class.'''
    return isinstance(obj, a_class)
