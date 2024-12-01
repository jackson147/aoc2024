def read_file_into_list(filename):
  """Reads a text file into a list, line by line.

  Args:
    filename: The name of the file to read.

  Returns:
    A list containing the lines of the file.
  """

  with open(filename, 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    return lines