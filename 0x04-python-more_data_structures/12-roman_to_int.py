#!/usr/bin/python3
def is_roman(string, romman_letters):
    for letter in string:
        if letter not in romman_letters:
            return (False)
    return (True)


def convert(string, roman_letters):
    flag, counter, result = 0, 0, 0
    size = len(string)

    for digit in string:
        if (flag):
            flag = 0
            counter += 1
            continue

        if (counter + 1 != size or counter == size):
            if (string[counter] == 'I' and string[counter + 1] == 'V'):
                result += 4
                flag = 1
            elif (string[counter] == 'I' and string[counter + 1] == 'X'):
                result += 9
                flag = 1
            elif (string[counter] == 'X' and string[counter + 1] == 'L'):
                result += 40
                flag = 1
            elif (string[counter] == 'X' and string[counter + 1] == 'C'):
                result += 90
                flag = 1
            elif (string[counter] == 'C' and string[counter + 1] == 'D'):
                result += 400
                flag = 1
            elif (string[counter] == 'C' and string[counter + 1] == 'M'):
                result += 900
                flag = 1
            else:
                result += roman_letters[digit]
                counter += 1
        else:
            result += roman_letters[digit]
            counter += 1
    return (result)


def roman_to_int(roman_string):
    roman_letters = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    if (roman_string is None):
        return (0)

    if (is_roman(roman_string, roman_letters)):
        return (convert(roman_string, roman_letters))
    return (0)
