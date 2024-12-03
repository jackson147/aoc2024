from utils import read_file_into_list
import re

# FILE = './example.txt'
FILE = './data.txt'

lines = read_file_into_list(FILE)

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

print(lines[0])


answer = 0
for line in lines:
    matches = re.findall(pattern, line)
    for val1, val2 in matches:
        answer += (int(val1)*int(val2))

# print(matches)
print(answer)