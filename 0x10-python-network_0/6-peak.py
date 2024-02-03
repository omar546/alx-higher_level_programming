#!/usr/bin/python3
"""Defines a peak-finding algorithm."""

def find_peak(list_of_integers):
    """Return the peak of a list of integers."""

    maxy = None
    for element in list_of_integers:
            if maxy is None or maxy < element:
                maxy = element
                return maxy
