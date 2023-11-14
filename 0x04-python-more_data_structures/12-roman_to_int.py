#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string.isalpha():
        roman_int_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman_reversed = roman_string[::-1]
        number = 0
        length = len(roman_string)
        for i in range(length):
            if roman_int_dict[roman_reversed[i]] < roman_int_dict[roman_reversed[i - 1]] and i -1 >= 0:
                number -= roman_int_dict[roman_reversed[i]]
            else:
                number += roman_int_dict[roman_reversed[i]]
    else:
        return 0
    return number
