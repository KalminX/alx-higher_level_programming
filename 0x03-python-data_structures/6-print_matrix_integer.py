#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    column = len(matrix[0])
    for i in range(row):
        for j in range(column):
            if j != column - 1:
                print("{}".format(matrix[i][j]), end=' ')
            else:
                print("{}".format(matrix[i][j]))
            j += 1
        i += 1
