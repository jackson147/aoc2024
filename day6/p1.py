import os
import sys
from guard import Guard
from utils import read_file_into_list

class Day6p1:
  def __init__(self, file):
        self._file = file
        self.matrix = [list(row) for row in read_file_into_list(self._file)]
        self.guard = self.find_guard()

  def _get_matrix_value(self, pos) -> str:
      x,y = pos
      return self.matrix[y][x]
  
  def _set_matrix_value(self, pos, char):
      x,y = pos
      self.matrix[y][x] = char

  def _is_move_within_bounds(self, new_pos):
      x, y = new_pos
      y_max_index = len(self.matrix) - 1
      x_max_index = len(self.matrix[0]) - 1
      return 0 <= y <= y_max_index and 0 <= x <= x_max_index

  def _is_obstacle(self, pos) -> bool:
      return self._get_matrix_value(pos) == '#'

  def find_guard(self) -> Guard:
      for y, row in enumerate(self.matrix):
          for x, el in enumerate(row):
              if el in ['^', '<', '>', 'V']:
                  return Guard((x,y), el)
              
  def rotate_guard(self):
    direction = self.guard.direction
    if direction == '^':
        direction = '>'
    elif direction == '>':
        direction = 'V'
    elif direction == 'V':
        direction = '<'
    elif direction == '<':
        direction = '^'
    else:
        raise Exception(f"Direction: {direction}, not recognised")
    
    self.guard.direction = direction
    self._set_matrix_value(self.guard.pos, self.guard.direction)
              
  def move_guard(self) -> bool:
    direction = self.guard.direction
    new_pos = self.guard.pos[:]
    x, y = new_pos
    if direction == '^':
        #Move up
        new_pos = (x, y-1)
    elif direction == '>':
        #Move right
        new_pos = (x+1, y)
    elif direction == 'V':
        #Move down
        new_pos = (x, y+1)
    elif direction == '<':
        #Move left
        new_pos = (x-1, y)
    else:
        raise Exception(f"Direction: {direction}, not recognised")
    
    if self._is_move_within_bounds(new_pos):
        if not self._is_obstacle(new_pos):
            # Guard has moved, leaves an X where they've just been
            self._set_matrix_value(self.guard.pos, 'X')
            self.guard.pos = new_pos
            # Set new guard on the matrix
            self._set_matrix_value(self.guard.pos, self.guard.direction)
        else:
            # Rotate guard handles its own matrix value set
            self.rotate_guard()
        
        # Guard is still within the matrix
        return True
    
    # Guard has left the area, set his last space as visited
    self._set_matrix_value(self.guard.pos, 'X')
    return False
  
  def count_guard_visited(self):
    count = 0
    for row in self.matrix:
        for col in row:
            if col == 'X':
                count += 1
    return count

if __name__ == '__main__':
    file = './example.txt'
    if len(sys.argv) >= 2:
        file = sys.argv[1]
    day = Day6p1(file)
    
    while(day.move_guard()):
        pass
    
    print(day.count_guard_visited())



