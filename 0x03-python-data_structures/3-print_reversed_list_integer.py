#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse_len = len(my_list) + 1
    for elem in range(1, reverse_len):
        print(my_list[-elem])
