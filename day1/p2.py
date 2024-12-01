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

answer = 0
for value in first_list:
    count_in_second = second_list.count(value)
    answer += value * count_in_second
print(answer)
