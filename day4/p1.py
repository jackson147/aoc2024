from utils import read_file_into_list
import re

FILE = './example.txt'
# FILE = './data.txt'

lines = read_file_into_list(FILE)

def print_matrix(matrix):
     for row in matrix:
          print(row)

def char_equal(matrix, x, y, char):
    return matrix[y][x] == char

def get_direction(coordinate, previous_coordinate):

    if(previous_coordinate is None):
        return None

    y,x = coordinate
    py, px = previous_coordinate

    if(x == px and y != py):
        if(y > py):
            return 'POSITIVE_Y'
        else:
            return 'NEGATIVE_Y'
    if(y == py and x != px):
        if(x > px):
            return 'POSITIVE_X'
        else:
            return 'NEGATIVE_X'
    
    if(x != px and y != py):
        if(y > py and x > px):
            return 'POSITIVE_BOTH'
        elif(y > py and x < px):
            return 'POSITIVE_Y_NEGATIVE_X'
        elif(y < py and x > px):
            return 'NEGATIVE_Y_POSITIVE_X'
        else:
            return 'NEGATIVE_BOTH'
    
    raise Exception("Can't get direction as there has been no movement")
    


def find_around_coordinate(matrix, coordinate, char, previous_coordinate=None):
    coordinates = []
    y, x = coordinate

    # Straight lines
    direction = get_direction(coordinate, previous_coordinate)
    if(x > 0 and (direction == 'NEGATIVE_X' or direction is None)):
        if(char_equal(matrix, x - 1, y, char)):
            coordinates.append((y, x-1, direction))
    if(y > 0 and (direction == 'NEGATIVE_Y' or direction is None)):
        if(char_equal(matrix, x, y - 1, char)):
            coordinates.append((y - 1, x, direction))
    if(x < len(matrix[0]) - 1 and (direction == 'POSITIVE_X' or direction is None)):
        if(char_equal(matrix, x + 1, y, char)):
            coordinates.append((y, x + 1, direction))
    if(y <  len(matrix) and (direction == 'POSITIVE_Y' or direction is None)):
        if(char_equal(matrix, x, y + 1, char)):
            coordinates.append((y + 1, x, direction))

    if(x > 0 and y > 0  and (direction == 'NEGATIVE_BOTH' or direction is None)):
        if(char_equal(matrix, x - 1, y - 1, char)):
            coordinates.append((y-1, x-1, direction))
    if(x < len(matrix[0]) - 1 and y <  len(matrix) - 1  and (direction == 'POSITIVE_BOTH' or direction is None)):
        if(char_equal(matrix, x + 1, y + 1, char)):
            coordinates.append((y+1, x+1, direction))
    if(x > 0 and y <  len(matrix) - 1  and (direction == 'POSITIVE_Y_NEGATIVE_X' or direction is None)):
        if(char_equal(matrix, x - 1, y + 1, char)):
            coordinates.append((y+1, x-1, direction))
    if(x < len(matrix[0]) - 1 and y > 0  and (direction == 'NEGATIVE_Y_POSITIVE_X' or direction is None)):
        if(char_equal(matrix, x + 1, y - 1, char)):
            coordinates.append((y-1, x+1, direction))

    return coordinates

def get_xmas_count(matrix, to_check, previous):
    y, x = to_check

    search_for = None

    # We are looking for an X value in this position
    if(previous is None):
        search_for = 'M'
    else:
        # Otherwise set the relevant value or error
        previous_char = matrix[x,y]
        if(previous_char == 'M'):
             search_for = 'A'
        elif(previous_char == 'A'):
             search_for = 'S'
        else:
             search_for = ''
    
    # Search for values around the coordinate
         

matrix = []
for line in lines:
    row = []
    for char in line:
         row.append(char)
    matrix.append(row)

# previous = None
# for i in range(0,len(matrix)):
#      for j in range(0, len(row)):
#           get_xmas_count(matrix, (i, j), previous)
#           previous = (i, j)

# print(get_direction((0,1), (0,0)))

# print(get_direction((1,1), (0,0)))

# print(get_direction((1,1), (2,2)))

print_matrix(matrix)

print(matrix[2][2])
print(find_around_coordinate(matrix, (2,2), 'M', None))
founds = find_around_coordinate(matrix, (2,2), 'M', None)
for found in founds:
    y, x, direction = found
    print(matrix[y][x])

