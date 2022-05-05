#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (0)

    cuantity = 0
    sum_grades = 0
    for grade in my_list:
        cuantity += grade[1]
        sum_grades += grade[0] * grade[1]

    return (sum_grades / cuantity)
