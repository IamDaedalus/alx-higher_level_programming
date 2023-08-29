#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    #return list(map((lambda row: list(map((lambda x: x ** 2), row))), matrix))
    if len(matrix) < 1:
        return []

    neo = []
    for i in range(len(matrix)):  # Loop through rows
        row = []
        for j in range(len(matrix[i])):  # Loop through columns
            row.append(matrix[i][j] ** 2)  # Calculate square and append to row
        neo.append(row)  # Append row to neo matrix

    return neo
