#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda sub_matrix:
                list(map(lambda i: i**2, sub_matrix)), matrix))
