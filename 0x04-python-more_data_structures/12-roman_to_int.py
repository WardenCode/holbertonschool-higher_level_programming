#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or len(roman_string) == 0:
        return (0)

    digits = {'I': 1, 'V': 5, 'X': 10,
              'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(roman_string)):
        if (i > 0) and (digits[roman_string[i]] > digits[roman_string[i - 1]]):
            result += digits[roman_string[i] - 2 * roman_string[i - 1]]
        else:
            result += digits[roman_string[i]]

    return result
