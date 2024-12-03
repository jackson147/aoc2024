from utils import read_file_into_list
import re

# FILE = './example_p2.txt'
FILE = './data.txt'

lines = read_file_into_list(FILE)

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

def remove_prefix_up_to_substring(string, substring):
  """Removes the prefix from a string up to and including the first occurrence of a substring.

  Args:
    string: The input string.
    substring: The substring to search for.

  Returns:
    The string without the prefix, or the original string if the substring is not found.
  """

  if substring in string:
    index = string.index(substring) + len(substring)
    return string[index:]
  else:
    return string

skip_next_mul = False
def parse_line(line):
    global skip_next_mul
    char_buffer=''

    total = 0
    for char in line:
        char_buffer = char_buffer + char

        print(char_buffer, skip_next_mul)

        mul_pattern_check = re.search(mul_pattern, char_buffer)
        if(bool(mul_pattern_check)):
            val1, val2 = mul_pattern_check.groups()
            if(not skip_next_mul):
                total += (int(val1) *  int(val2))
            char_buffer = remove_prefix_up_to_substring(char_buffer, mul_pattern_check.string)
        elif(re.search('don\'t\(\)', char_buffer)):
            skip_next_mul = True
            char_buffer = remove_prefix_up_to_substring(char_buffer, "don't()")
        elif(re.search('do\(\)', char_buffer)):
            skip_next_mul = False
            char_buffer = remove_prefix_up_to_substring(char_buffer, 'do()')

    return total

answer = 0
full_line = ''
for line in lines:
  full_line += line

answer = parse_line(full_line)
print(answer)