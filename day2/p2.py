from utils import read_file_into_list, print_array

# FILE = './example.txt'
FILE = './data.txt'


lines = read_file_into_list(FILE)

def is_safe_line(line):
    is_increasing = line[1] > line[0]
    if(line[1] == line[0]):
        return False

    for i in range(0, len(line) - 1):

        first = line[i]
        second = line[i+1]

        diff = abs(first - second)

        if diff == 0 or diff > 3 or (is_increasing and first > second) or (not is_increasing and first < second):
            return False
    return True

safe_lines = 0
failed_lines = []
for line in lines:
    if(is_safe_line(line)):
        safe_lines+=1
    else:
        failed_lines.append(line)

failed_transformations = 0
for f_line in failed_lines:
    for i in range(0, len(f_line)):
        f_line_copy = f_line.copy()
        f_line_copy.pop(i)
        if(is_safe_line(f_line_copy)):
            failed_transformations += 1
            break

print(failed_transformations + safe_lines)
