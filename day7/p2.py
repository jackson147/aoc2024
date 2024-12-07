from collections import defaultdict
import sys
from utils import read_file_into_list
from functools import reduce
from operator import mul
import time


class Part2:
    def __init__(self, file):
        self._file = file
        self._data = read_file_into_list(self._file)
        self.parse_input_data(self._data)

    def parse_input_data(self, data):
        parsed_data = defaultdict(list)
        for line in data:
            split_line = line.split(":")
            split_values = list(map(int, split_line[1].strip().split(" ")))
            parsed_data[split_line[0]] = split_values
        self.data = parsed_data

    def is_possible(self, result_key, input_equation_values=None):
        if input_equation_values:
            equation_values = input_equation_values
        else:
            equation_values = self.data[result_key]

        product = reduce(mul, equation_values)
        return product >= int(result_key)

    def generate_permutations(self, arr, n, index):
        if index == n:
            return [arr.copy()]

        permutations = []
        arr[index] = "+"
        permutations.extend(self.generate_permutations(arr, n, index + 1))

        arr[index] = "*"
        permutations.extend(self.generate_permutations(arr, n, index + 1))

        arr[index] = "|"
        permutations.extend(self.generate_permutations(arr, n, index + 1))

        return permutations


if __name__ == "__main__":
    file = "./example.txt"
    if len(sys.argv) >= 2:
        file = sys.argv[1]
    day = Part2(file)

    valid_equation_keys = []
    # possible_keys = list(filter(day.is_possible, day.data))
    possible_keys = day.data
    # print(possible_keys)
    possibly_correct_operator_sum = 0
    for result_key in possible_keys:
        equation = day.data[result_key]
        operators_length = len(equation) - 1
        initial_arr = [None] * operators_length
        operator_permutations = day.generate_permutations(
            initial_arr, operators_length, 0
        )

        for z, operator_perm in enumerate(operator_permutations):
            string_equation = f"{equation[0]}"
            non_bodmas_result = equation[0]
            for i in range(1, len(equation)):
                string_equation += f" {operator_perm[i-1]} {equation[i]}"
                if operator_perm[i - 1] == "+":
                    non_bodmas_result += equation[i]
                elif operator_perm[i - 1] == "|":
                    non_bodmas_result = int(f"{non_bodmas_result}{equation[i]}")
                else:
                    non_bodmas_result *= equation[i]
            # equation_result = eval(string_equation)

            # print(string_equation, "=", non_bodmas_result)
            # time.sleep(0.5)

            if non_bodmas_result == int(result_key):
                possibly_correct_operator_sum += int(result_key)
                break

            if z == len(operator_permutations) - 1:
                print(result_key, string_equation, non_bodmas_result)
    print(possibly_correct_operator_sum)
