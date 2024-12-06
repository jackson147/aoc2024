import os
import sys
from typing import Tuple
from guard import Guard
from utils import read_file_into_list, print_matrix
import multiprocessing

class Day6p2:
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
      return self._get_matrix_value(pos) in ['#', 'O']
  
  def get_matrix_size(self):
      return (len(self.matrix[0]), len(self.matrix))

  def find_guard(self) -> Guard:
      for y, row in enumerate(self.matrix):
          for x, el in enumerate(row):
              if el in ['^', '<', '>', 'V']:
                  return Guard((x,y), el)

  def get_rotation(self, direction):
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
    return direction
              
  def rotate_guard(self):
    direction = self.get_rotation(self.guard.direction)
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

  def get_next_guard(self) -> Guard:
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
    
    # Need to handle out of bounds outside of this function
    if not self._is_obstacle(new_pos):
        # Guard WILL moved into next pos
        return Guard(new_pos, direction)
    return Guard(self.guard.pos, self.get_rotation(direction))

  def count_guard_visited(self):
    count = 0
    for row in self.matrix:
        for col in row:
            if col == 'X':
                count += 1
    return count

def is_guard_looping(obstruction) -> bool:
    x,y = obstruction
    day = Day6p2(file)
    serialised_starting_guard = day.find_guard().seralise()
    # Add the starting location to the path
    path = [serialised_starting_guard]
    # Set obstacle in matrix
    day._set_matrix_value((x,y), 'O')
    # Set the the guard moving
    while(day.move_guard()):
        seralised_guard = day.guard.seralise()
        # We have been in this position and with this direction before!
        if(seralised_guard in path):
            return True
        # Otherwise add the path and continue
        path.append(seralised_guard)
    return False

if __name__ == '__main__':
    file = './example.txt'
    if len(sys.argv) >= 2:
        file = sys.argv[1]
    day = Day6p2(file)
    
    serialised_starting_guard = day.find_guard().seralise()
    x_size, y_size = day.get_matrix_size()
    guard_stuck_in_loop_counter = 0
    
    obstruction_locations = []
    for x in range(x_size):
        for y in range(y_size):
            obstruction_locations.append((x,y))
            # # Add the starting location to the path
            # path = [serialised_starting_guard]
            # # Set obstacle in matrix
            # day._set_matrix_value((x,y), 'O')
            # # Set the the guard moving
            # while(day.move_guard()):
            #     seralised_guard = day.guard.seralise()
            #     # We have been in this position and with this direction before!
            #     if(seralised_guard in path):
            #         # Increment guard loop counter
            #         guard_stuck_in_loop_counter += 1
            #         break
            #     # Otherwise add the path and continue
            #     path.append(seralised_guard)
                
            # # Reset everything and go again
            # # print_matrix(day.matrix)
            # path.clear()
            # day = Day6p2(file)
                
    # print(guard_stuck_in_loop_counter)
    
    pool = multiprocessing.Pool()
    results = pool.map(is_guard_looping, obstruction_locations)
    pool.close()
    pool.join()

    print(sum(results))
    
                
                
                
                
                    
            
    
    
    



