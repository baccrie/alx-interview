#!/usr/bin/python3

"""
Pascal Triangle Interview
"""


def pascal_triangle(n):
    """A function that returns a list of list of integers
    representing the pascal triangle
    """
    list_of_list = []
    prev_list = []

    for i in range(1, n+1):
        if i == 1:
            prev_list = [1]
            list_of_list.append(prev_list)
        elif (i == 2):
            prev_list = [1, 1]
            list_of_list.append(prev_list)
        else:
            present_list = []
            for j in range(1, i+1):
                if j == 1 or j == i:
                    present_list.append(1)
                else:
                    item = prev_list[j - 1] + prev_list[j - 2]
                    present_list.append(item)
            prev_list = present_list
            list_of_list.append(prev_list)

    return list_of_list
