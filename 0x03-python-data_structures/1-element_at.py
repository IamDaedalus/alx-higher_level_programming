#!/usr/bin/python3

def element_at(my_list, idx):
    """Fetches an element at index of idx

    Args:
        my_list: the list from which to fetch the
        element
        idx: the index of the element to fetch
    """
    length = len(my_list) - 1

    if idx < 0 or idx > length:
        return None
    else:
        return my_list[idx]
