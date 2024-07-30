import sys
import math

def main():
    circle_filepath = ""
    dots_filepath  = ""
    if len(sys.argv) == 3:
        circle_filepath = sys.argv[1]
        dots_filepath = sys.argv[2]
    else:
        circle_filepath = input()
        dots_filepath = input()
    with open(circle_filepath) as circle_file:
        center = list(map(int, circle_file.readline().split()))
        radius = int(circle_file.readline())
    with open(dots_filepath) as dots_file:
        lines = dots_file.readlines()
    for line in lines:
        dot = list(map(int, line.split()))
        distance = math.dist(center, dot) 
        if distance == radius:
            print("0")
        elif distance < radius:
            print("1")
        else:
            print("2")

if __name__ == "__main__":
    main()