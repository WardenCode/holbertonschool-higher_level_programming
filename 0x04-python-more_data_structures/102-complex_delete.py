#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    entries = a_dictionary.items()
    to_elimitate = []

    for actual_key, actual_value in entries:
        if value == actual_value:
            to_elimitate.append(actual_key)

    for key in to_elimitate:
        del a_dictionary[key]

    return (a_dictionary)
