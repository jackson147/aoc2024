from collections import defaultdict
import sys
from utils import read_file_into_list


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


if __name__ == "__main__":
    file = "./example.txt"
    if len(sys.argv) >= 2:
        file = sys.argv[1]
    day = Part2(file)
