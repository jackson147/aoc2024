from utils import read_file_into_list
import matplotlib.pyplot as plt
import numpy as np

# FILE = './example_p2.txt'
FILE = './data.txt'

lines = read_file_into_list(FILE)

matrix = []
for line in lines:
    row = []
    for char in line:
         row.append(char)
    matrix.append(row)

def print_matrix(matrix):
     for row in matrix:
          print(row)

# Just checking for M and S
def contains_xmas(candidate):
    # print(candidate)
    return len(candidate) == 2 and 'M' in candidate and 'S' in candidate

def get_char(matrix, x, y):
     return matrix[y][x]

def check_coordinate(x, y):
    target = get_char(matrix, x, y)
    # Target must equal A
    if(target != 'A'):
        return False
    
    # Can't get diag values if we're at a bondary
    if(x == 0 or y == 0 or x == len(matrix[0]) - 1 or y == len(matrix) - 1):
        return False
     
    # Top left bottom right
    tl_br_candidate = get_char(matrix, x-1, y-1) + get_char(matrix, x+1, y+1)
    # Top right bottom left
    tr_bl_candidate = get_char(matrix, x+1, y-1) + get_char(matrix, x-1, y+1)
    return contains_xmas(tl_br_candidate) and contains_xmas(tr_bl_candidate)

total = 0
for x in range(len(matrix[0])):
    for y in range(len(matrix)):
        if(check_coordinate(x, y)):
            total += 1

print(total)