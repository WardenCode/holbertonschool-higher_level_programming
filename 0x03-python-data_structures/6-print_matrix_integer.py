#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not len(matrix[0]):
        print("")
        return (None)

    for row in matrix:
        for el in row:
            print("{:d}".format(el), end=("\n" if (el == row[-1]) else " "))
