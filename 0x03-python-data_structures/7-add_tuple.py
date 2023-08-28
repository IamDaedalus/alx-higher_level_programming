#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    max_len = max(len(tuple_a), len(tuple_b))
    tup = []

    for i in range(max_len):
        value_a = tuple_a[i] if i < len(tuple_a) else 0
        value_b = tuple_b[i] if i < len(tuple_b) else 0
        tup.append(value_a + value_b)

    return tuple(tup)
