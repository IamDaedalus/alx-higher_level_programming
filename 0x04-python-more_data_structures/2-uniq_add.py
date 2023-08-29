#!/usr/bin/python3

def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return 0

    ret_val = 0
    my_set = set()
    for i in range(0, len(my_list)):
        if my_set.__contains__(my_list[i]):
            continue
        else:
            ret_val = ret_val + my_list[i]
            my_set.add(my_list[i])

    return ret_val
