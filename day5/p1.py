from utils import read_file_into_list

# FILE = './example.txt'
FILE = './data.txt'

lines = read_file_into_list(FILE)

rules = []
updates = []
for line in lines:
    if('|' in line):
        rules.append(list(map(int, tuple(line.split('|')))))
    elif(',' in line):
        updates.append(list(map(int,line.split(','))))

# print(rules)
# print(updates)

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

def is_valid_update(update, rules):
    for rule in rules:
        before, after = rule

        if before in update and after in update:
            index_before = update.index(before)
            index_after = update.index(after)
            if index_after < index_before:
                return False
    return True

middle_sum = 0
for update in updates:
    if(is_valid_update(update, rules)):
        middle_sum += middle_element(update)
print(middle_sum)

# print(is_valid_update([75,47,61,53,29], rules))
# print(is_valid_update([61,13,29], rules))
            


