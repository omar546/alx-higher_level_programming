#!/usr/bin/python3
def multiply_by_2(my_dict):
    tmp = my_dict.copy()
    for x in tmp.keys():
        tmp[x] *= 2
    return (tmp)
