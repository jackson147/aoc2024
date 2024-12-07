import os


def read_file_into_list(filename):
    """Reads a text file into a list, line by line.

    Args:
      filename: The name of the file to read.

    Returns:
      A list containing the lines of the file.
    """

    filename = os.path.abspath(filename)

    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines()]
        return lines


def print_array(array):
    for x in array:
        print(x)


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))
