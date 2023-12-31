#!/usr/bin/python3
"""
    add integers
    Args:
        a: first arg; its type must be int or float.
        b: second arg; default is 98. And if given must be int or float
"""

def add_integer(a, b=98):
    """
        Returns integer result
    """
    type_list = [int, float]
    error_msg_a = "a must be an integer"
    error_msg_b = "b must be an integer"

    if (type(a) not in type_list):
        raise TypeError(error_msg_a)

    if (type(b) not in type_list):
        raise TypeError(error_msg_b)

    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)

    return (a + b)
