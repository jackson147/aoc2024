from utils import read_file_into_list
import re

FILE = './example.txt'
# FILE = './data.txt'

lines = read_file_into_list(FILE)

def print_matrix(matrix):
     for row in matrix:
          print(row)

def diagonal_iteration(matrix, start_corner='top_left'):
  """Iterates through a matrix diagonally, starting from a specified corner.

  Args:
    matrix: A 2D matrix.
    start_corner: The corner to start from, can be 'top_left', 'top_right', 'bottom_left', or 'bottom_right'.

  Yields:
    Tuples of elements along each diagonal.
  """

  rows, cols = len(matrix), len(matrix[0])

  if start_corner == 'top_left':
    for i in range(rows + cols - 1):
      start_row = max(0, i - cols + 1)
      start_col = max(0, cols - i - 1)
      diagonal = []
      for j in range(min(i + 1, rows, cols)):
        diagonal.append(matrix[start_row + j][start_col + j])
      yield diagonal
  elif start_corner == 'top_right':
    for i in range(rows + cols - 1):
      start_row = max(0, i - cols + 1)
      start_col = min(cols - 1, i)
      diagonal = []
      for j in range(min(i + 1, rows, cols)):
        diagonal.append(matrix[start_row + j][start_col - j])
      yield diagonal
  elif start_corner == 'bottom_left':
    for i in range(rows + cols - 1):
      start_row = min(rows - 1, i)
      start_col = max(0, cols - i - 1)
      diagonal = []
      for j in range(min(i + 1, rows, cols)):
        diagonal.append(matrix[start_row - j][start_col + j])
      yield diagonal
  elif start_corner == 'bottom_right':
    for i in range(rows + cols - 1):
      start_row = min(rows - 1, i)
      start_col = min(cols - 1, i)
      diagonal = []
      for j in range(min(i + 1, rows, cols)):
        diagonal.append(matrix[start_row - j][start_col - j])
      yield diagonal
  else:
    raise ValueError("Invalid start_corner value. Please choose from 'top_left', 'top_right', 'bottom_left', or 'bottom_right'.")

matrix = []
for line in lines:
    row = []
    for char in line:
         row.append(char)
    matrix.append(row)

print_matrix(matrix)
for diagonal in diagonal_iteration(matrix, start_corner='top_right'):
  print(diagonal)

