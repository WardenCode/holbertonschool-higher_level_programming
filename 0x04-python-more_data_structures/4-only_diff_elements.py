#!/usr/bin/python3
def df(first_group, second_group):
    new_set = set()
    for elem in first_group:
        if elem not in second_group:
            new_set.add(elem)
    return (new_set)


def only_diff_elements(set_1, set_2):
    return (df(set_1, set_2) if len(set_1) >= len(set_2) else df(set_2, set_1))
