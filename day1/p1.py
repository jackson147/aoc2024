from utils import read_file_into_list
import re

data_file = './data.txt'

lines = read_file_into_list(data_file)

first_list = []
second_list = []
for line in lines:
    line_split = (re.split(r'\s+', line))
    first_list.append(int(line_split[0]))
    second_list.append(int(line_split[1]))

first_sorted = sorted(first_list)
second_sorted = sorted(second_list)

# print(first_sorted)

answer = 0
for x in range(0, len(first_list)):
    # print(first_sorted[x], second_sorted[x])
    answer += abs(first_sorted[x] - second_sorted[x])
    
print(answer)