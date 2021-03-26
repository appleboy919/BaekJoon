import sys


def sort_inside(n):
    length = len(n) - 1
    counts = [0] * 10
    for i in range(length):
        counts[9 - int(n[i])] += 1
    for i in range(10):
        while counts[i] > 0:
            sys.stdout.write(str(9 - i))
            counts[i] -= 1


if __name__ == '__main__':
    N = sys.stdin.readline()
    sort_inside(N)
