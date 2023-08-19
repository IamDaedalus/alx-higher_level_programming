#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element in a list

    Args:
        my_list: the list
        idx: the index at which to make the change
        element: the new element
    """
    length = len(my_list) - 1

    if idx < 0 or idx > length:
        return my_list
    else:
        my_list[idx] = element
        return my_list
