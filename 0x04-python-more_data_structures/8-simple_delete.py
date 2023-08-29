#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if len(a_dictionary) == 0:
        return

    if key in a_dictionary:
        del a_dictionary[key]
