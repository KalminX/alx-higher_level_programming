#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_list_copy = my_list.copy()

    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_list_copy[idx] = element
        return my_list_copy
