#!/usr/bin/python3
"""Defines a peak-finding algorithm."""

def find_peak(list_of_integers):
    """Return the peak of a list of integers."""
    size = len(list_of_integers)
    if size == 0:
        return None
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    
    middle = size // 2
    peak = list_of_integers[middle]

    # Handling edge cases for index out of bounds
    left_neighbor = list_of_integers[middle - 1] if middle - 1 >= 0 else float("-inf")
    right_neighbor = list_of_integers[middle + 1] if middle + 1 < size else float("-inf")

    if peak > left_neighbor and peak > right_neighbor:
        return peak
    elif peak < left_neighbor:
        return find_peak(list_of_integers[:middle])
    else:
        return find_peak(list_of_integers[middle + 1:])
