import sys

def print_sorted_coordinates(n):
    coordinates = []
    for i in range(n):
        coordinates.append(tuple(map(int, sys.stdin.readline().split())))


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    print_sorted_coordinates(N)