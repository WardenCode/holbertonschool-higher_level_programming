#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_a, length_b = len(tuple_a), len(tuple_b)
    num1, num2 = 0, 0

    if (length_a >= 2):
        num1 += tuple_a[0]
        num2 += tuple_a[1]
    elif (length_a == 1):
        num1 += tuple_a[0]

    if (length_b >= 2):
        num1 += tuple_b[0]
        num2 += tuple_b[1]
    elif (length_b == 1):
        num1 += tuple_a[0]

    new_tuple = (num1, num2)
    return (new_tuple)
