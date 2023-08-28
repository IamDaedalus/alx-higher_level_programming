#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints each element of a list
    Args:
        my_list: the list to print
    """
    for i in my_list:
        print("{:d}".format(i))
