#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints each element of a list
    Args:
        my_list: the list to print
    """
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
