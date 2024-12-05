def find_all_xmas(grid):
  """
  Finds all occurrences of the word "XMAS" in a word search grid.

  Args:
      grid: A list of strings representing the rows of the word search.

  Returns:
      The number of times "XMAS" appears in the grid.
  """
  count = 0
  rows, cols = len(grid), len(grid[0])

  # Check all directions (horizontal, vertical, diagonal) and both directions
  directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
  for word in ["XMAS", "SMXA"]:  # Check for both XMAS and its reverse
    for row in range(rows):
      for col in range(cols):
        for dr, dc in directions:
          current_row, current_col = row, col
          found = True
          for char in word:
            if 0 <= current_row < rows and 0 <= current_col < cols and grid[current_row][current_col] == char:
              current_row += dr
              current_col += dc
            else:
              found = False
              break
          if found:
            count += 1

  return count


from utils import read_file_into_list
import re

FILE = './example.txt'
# Get your puzzle input as a list of strings (one string per row)
puzzle_input = read_file_into_list(FILE)
# ... (replace this with your actual puzzle input lines)

# Find and print the number of occurrences of "XMAS"
num_xmas = find_all_xmas(puzzle_input)
print(f"The word 'XMAS' appears {num_xmas} times in the word search.")