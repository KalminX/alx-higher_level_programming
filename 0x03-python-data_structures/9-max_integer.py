#!/usr/bin/python3
def max_integer(my_list=[]):
    len1 = len(my_list)
    if len1 == 0:
        return None
    else:
        my_list.sort()
        return my_list[-1]
