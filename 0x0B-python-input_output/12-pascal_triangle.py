#!/usr/bin/python3
"""12-pascal_triangle"""

def pascal_triangle(n):
    """ Function to return the pascal triangle

    Args:
        n: n-lines

    Returns:
        matrix: the pascal triangle matrix

    """

    matrix = []
    prev = []

    for i in range(n):
        res_list = []
        p1 = -1
        p2 = 0
        for j in range(len(prev) + 1):
            if p1 == -1 or p2 == len(prev):
                res_list += [1]
            else:
                res_list += [prev[p1] + prev[p2]]
            p1 += 1
            p2 += 1
        matrix.append(res_list)
        prev = res_list[:]

    return matrix
