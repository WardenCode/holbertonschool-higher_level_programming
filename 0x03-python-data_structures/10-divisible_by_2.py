#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for num in my_list:
        res = -(-num % 2) if num < 0 else num % 2
        new_list.append(True if res == 0 else False)

    return (new_list)
