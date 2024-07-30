import sys
import math


def main():
    array_filepath = ""
    if len(sys.argv) == 2:
        array_filepath = sys.argv[1]
    else:
        array_filepath = input()
    with open(array_filepath) as array_file:
        array = []
        count = 0
        for line in array_file.readlines():
            count += 1
            array.append(int(line))
    if (count == 0): return
    average = sum(array) / count
    remainder = average % 1
    to_num = 0
    if (remainder >= 0.5):
        to_num = math.ceil(average)
    else:
        to_num = math.floor(average)
    changes = 0
    for number in array:
        changes += math.fabs(to_num - number)
    print(int(changes))
if __name__ == "__main__":
    main()