#!/usr/bin/python3
"""My class module"""


def pascal_triangle(n):
    """My pascal triangle function"""
    triangle = []

    for row_number in range(n):
        current_row = []

        for element in range(row_number + 1):
            if element == 0 or element == row_number:
                current_row.append(1)
            else:
                value = triangle[row_number - 1][element] + \
                    triangle[row_number - 1][element - 1]
                current_row.append(value)

        triangle.append(current_row)

    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
