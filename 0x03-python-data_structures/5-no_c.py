#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    length = len(string_list) - 1
    i = 0
    while i <= length:
        if string_list[i] == 'c' or string_list[i] == 'C':
            del string_list[i]
            length -= 1
            i -= 1
        i += 1
    new_string = ''.join(string_list)
    return new_string
