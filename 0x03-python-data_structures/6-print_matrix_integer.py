#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return (None)
    for row in matrix:
        for element in row:
            if (element == row[-1]):
                print(element)
            else:
                print(element, end=" ")
