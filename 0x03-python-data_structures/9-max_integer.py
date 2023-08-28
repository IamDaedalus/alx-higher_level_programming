#!/usr/bin/python3

def max_integer(my_list=[]):
    """This finds the maximum value in a list

    Args:
        my_list: the list to check
    """
    if len(my_list) == 0:
        return None

    val = 0
    for i in range(len(my_list)):
        if my_list[i] > val:
            val = my_list[i]

    return val

