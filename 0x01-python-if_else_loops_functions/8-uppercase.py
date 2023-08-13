#!/usr/bin/python3

def islower(c):
    """Returns True if c is a lowercase letter

    False otherwise.
    """
    return ord(c) >= ord('a') and ord(c) <= ord('z')


def uppercase(str):
    """This function prints str in uppercase"""
    new_str = ""
    for ch in str:
        if islower(ch):
            new_str += chr(ord(ch) - 32)
        else:
            new_str += ch
    print("{}".format(new_str))
