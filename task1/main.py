import sys


def main():
    max_num = 0
    interval = 0
    if len(sys.argv) == 3:
        max_num = int(sys.argv[1])
        interval = int(sys.argv[2]) - 1
    else:
        max_num = int(input())
        interval = int(input()) - 1
    array = list(range(1, max_num + 1))
    index = interval % max_num
    digits = "1"
    while index != 0:
        digits += str(array[index])
        index = (index + interval) % max_num
    print(digits)

if __name__ == "__main__":
    main()