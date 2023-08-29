#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if len(a_dictionary) == 0:
        return

    a_dictionary[key] = value
