from utils import read_file_into_list

# FILE = './example.txt'
FILE = './data.txt'


lines = read_file_into_list(FILE)

def is_safe_line(line, is_second_call):
    is_increasing = line[1] > line[0]
    if(line[1] == line[0]):
        return False

    for i in range(0, len(line) - 1):

        first = line[i]
        second = line[i+1]

        diff = abs(first - second)

        if diff == 0 or diff > 3 or (is_increasing and first > second) or (not is_increasing and first < second):
            if(is_second_call):
                return False
            
            line_copy_first = line.copy()
            line_copy_second = line.copy()
            line_copy_first.pop(i)
            line_copy_second.pop(i+1)
            print(line)
            print(line_copy_first, is_safe_line(line_copy_first, True))
            print(line_copy_second, is_safe_line(line_copy_first, True))
            print()
            
            return is_safe_line(line_copy_first, True) or is_safe_line(line_copy_second, True)
    return True

safe_lines = 0
for line in lines:
    if(is_safe_line(line, False)):
        safe_lines+=1
print(safe_lines)