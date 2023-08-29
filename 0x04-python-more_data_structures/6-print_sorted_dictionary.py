#!/usr/bin/python

def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) == 0:
        return

    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
