def read_file_into_list(filename):
  """Reads a text file into a list, line by line.

  Args:
    filename: The name of the file to read.

  Returns:
    A list containing the lines of the file.
  """

  with open(filename, 'r') as f:
    lines = [list(map(int, line.strip().split(' '))) for line in f]
  return lines

def print_array(array):
  for x in array:
    print(x)