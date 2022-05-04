#!/usr/bin/python3
def df(first_group, second_group):
    new_set = set()
    for elem in first_group:
        if elem not in second_group:
            new_set.add(elem)
    return (new_set)


def only_diff_elements(set_1, set_2):
    len_1 = len(set_1)
    len_2 = len(set_2)

    if len_1 == 0 and len_2 == 0:
        return (set())
    elif len_1 == 0:
        return (set_2)
    elif len_2 == 0:
        return (set_1)

    return (df(set_1, set_2) if len_1 >= len_2 else df(set_2, set_1))
