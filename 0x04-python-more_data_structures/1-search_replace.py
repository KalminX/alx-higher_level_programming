#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    if search in my_list:
        number = my_list.index(search)
        new_list[number] = replace
    return new_list
