#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Creates a new list and changes the element at
    idx

    Args:
        my_list: the list to copy
        idx: the index at which to make the change
        element: the new element to insert

    Returns a new list with the changed element
    """
    new_list = my_list[:]
    length = len(new_list) - 1

    if idx < 0 or idx > length:
        return my_list

    new_list[idx] = element
    return new_list
