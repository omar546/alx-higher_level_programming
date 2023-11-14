#!/usr/bin/python3

'''1. My list'''


class MyList(list):
    '''class MyList'''
    def print_sorted(self):
        '''Function to print the sorted list,
        (ascending sort)'''
        print(sorted(self))
