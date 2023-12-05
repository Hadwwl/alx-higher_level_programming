#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for minimatrix in matrix:
        if len(minimatrix) == 0:
            print()
        for i in range(len(minimatrix)):
            print("{:d}".format(minimatrix[i]),
                  end='\n' if i is len(minimatrix) - 1 else " ")
