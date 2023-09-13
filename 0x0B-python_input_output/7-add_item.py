#!/usr/bin/python3
"""This module extracts all arguments from the commandline
and stores them in a json file
"""

import sys
save_json = __import__('5-save_to_json_file').save_to_json_file
from_json = __import__('6-load_from_json_file').load_from_json_file


"""main entry for this script"""
if __name__ == "__main__":
    my_list = []
    # extract the every argument but the first from argv
    args = sys.argv[1:]
    for i, arg in enumerate(args):
        my_list.append(arg)

    # save and load the json file
    save_json(my_list, "add_item.json")
    from_json("add_item.json")
