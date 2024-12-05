from utils import read_file_into_list

# FILE = './example_simple.txt'
# FILE = './example.txt'
FILE = './data.txt'

lines = read_file_into_list(FILE)

def print_matrix(matrix):
     for row in matrix:
          print(row)

def get_diagonals(grid, bltr = True):
  dim = len(grid)
  assert dim == len(grid[0])
  return_grid = [[] for total in range(2 * len(grid) - 1)]
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if bltr: return_grid[row + col].append(grid[col][row])
      else:    return_grid[col - row + (dim - 1)].append(grid[row][col])
  return return_grid

def count_overlapping(text, substring):
    count = 0
    for i in range(len(text) - len(substring) + 1):
        check_string = text[i:i+len(substring)]
        if check_string == substring:
            count += 1
    return count

def count_xmas(text):
   return count_overlapping(text, 'XMAS') + count_overlapping(text, 'SAMX')

matrix = []
for line in lines:
    row = []
    for char in line:
         row.append(char)
    matrix.append(row)

# print_matrix(matrix)
# print()
# for diagonal in get_diagonals(matrix):
#   print(diagonal)
# print()
# for diagonal in get_diagonals(matrix, False):
#   print(diagonal)

total = 0
# Horizontail
for row in matrix:
  joined_row = ''.join(row)
  count = count_xmas(joined_row)
  total += count

# vertical
for x in range(len(matrix[0])):
  joined_col = ''
  for y in range(len(matrix)):
    joined_col += matrix[y][x]
  count = count_xmas(joined_col)
  total += count

for diag in get_diagonals(matrix, True):
    joined_diag = ''.join(diag)
    count = count_xmas(joined_diag)
    total += count

for diag in get_diagonals(matrix, False):
    joined_diag = ''.join(diag)
    count = count_xmas(joined_diag)
    total += count

# print(matrix)
print(total)

    
