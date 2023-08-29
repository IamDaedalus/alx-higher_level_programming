#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return

    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2

    return new_dictionary
