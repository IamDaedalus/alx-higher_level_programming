#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Print elements of a matrix

    Args:
        matrix: the matrix to print
    """
    # iterate over each list in the list
    for i in range(len(matrix)):
        # iterate over each element in each lis
        for j in range(len(matrix[i])):
            print("{}".format(matrix[i][j]), end="")
            # check if 
            if j < len(matrix[i]) - 1:
                print(" ", end="")

        if i < len(matrix):
            print("$")
