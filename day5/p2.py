from utils import read_file_into_list
import copy
from collections import defaultdict, deque

# FILE = './example.txt'
FILE = './data.txt'

lines = read_file_into_list(FILE)

rules = []
raw_rules = []
updates = []
for line in lines:
    if('|' in line):
        raw_rules.append(line.strip('\n'))
        rules.append(list(map(int, tuple(line.split('|')))))
    elif(',' in line):
        updates.append(list(map(int,line.split(','))))

# I had to cheat here, but atleast I learnt a lot about toposort.
# Credit: https://github.com/womogenes/AoC-2024-Solutions/blob/main/day_05/p2_day_05.py#L24
def sort_correctly(update, rules):
    my_rules = []
    for a, b in rules:
        if not (a in update and b in update):
            continue
        my_rules.append((a, b))

    indeg = defaultdict(int)
    for a, b in my_rules:
        indeg[b] += 1
    
    ans = []
    while len(ans) < len(update):
        for x in update:
            if x in ans:
                continue
            if indeg[x] <= 0:
                ans.append(x)
                for a, b in my_rules:
                    if a == x:
                        indeg[b] -= 1
    
    return ans

def middle_element(lst):
  """Returns the middle element of a list.

  Args:
    lst: The input list.

  Returns:
    The middle element if the list length is odd,
    otherwise the average of the two middle elements.
  """

  middle_index = len(lst) // 2
  if len(lst) % 2 == 0:
    # Even length: average of two middle elements
    return (lst[middle_index - 1] + lst[middle_index]) / 2
  else:
    # Odd length: single middle element
    return lst[middle_index]

def swap_elements(my_list, index1, index2):
  """Swaps two elements in a list by their indices.

  Args:
    my_list: The list to modify.
    index1: The index of the first element to swap.
    index2: The index of the second element to swap.
  """

  if index1 >= len(my_list) or index2 >= len(my_list):
    raise Exception("Invalid indices")

  my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def is_valid_update(update, rules):
    for rule in rules:
        before, after = rule

        if before in update and after in update:
            index_before = update.index(before)
            index_after = update.index(after)
            if index_after < index_before:
                return False
    return True

def fix_invalid_update(update, rules):
    corrected_update = copy.copy(update)
    while(not is_valid_update(corrected_update, rules)):
       for rule in rules:
        before, after = rule

        if before in corrected_update and after in corrected_update:
            index_before = update.index(before)
            index_after = update.index(after)
            if index_after < index_before:
                swap_elements(corrected_update, index_before, index_after)
                
    return corrected_update

middle_sum = 0
for update in updates:
  if(not is_valid_update(update, rules)):
    sorted_update = sort_correctly(update, rules)
    middle_sum += middle_element(sorted_update)
print(middle_sum)



