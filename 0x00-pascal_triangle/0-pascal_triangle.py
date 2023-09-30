#!/usr/bin/python3
""" Pascal's triangle"""


def create_list(my_list):
    """
    Creates a list of Pascal integers from a previous list
    Args:
        my_list(list): list of previous integers
    """
    new_list = []
    for i in range(len(my_list)):
        if i == 0 or i == (len(my_list) - 1):
            new_list.append(my_list[i])

        if i < len(my_list) - 1:
            new_list.append(my_list[i] + my_list[i + 1])

    return new_list


def pascal_triangle(n):
    """
    Returns a list of integers representing Pascal's triangle of n

    Args:
        n(int): A number of Pascal's triangle
    """
    if n <= 0:
        return []

    big_list = []
    for num in range(1, n):
        if num == 1:
            big_list.append([1])
        elif num == 2:
            big_list.append([1, 2, 1])
        else:
            big_list.append(create_list(big_list[num - 2]))
    return big_list
