#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 == 0:
        tuple_a = (0, 0)
    if len2 == 0:
        tuple_b = (0, 0)
    if len1 == 1:
        tuple_a = (tuple_a[0], 0)
    if len2 == 1:
        tuple_b = (tuple_b[0], 0)
    sum1 = tuple_a[0] + tuple_b[0]
    sum2 = tuple_a[1] + tuple_b[1]
    return sum1, sum2
