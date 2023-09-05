#!/usr/bin/python3

"""This module divides all elements in a matrix"""


def matrix_divided(matrix, div):
    """Function to divide each element in a matrix
    by a div

    Args:
        matrix: the matrix whose elements we divide
        div: the dividend for each element in the matrix
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
