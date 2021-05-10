import sys


def print_N_queens(n):
    board = [True] * n * n
    row = col = n - 1
    # TODO: check diagonal??


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    print_N_queens(N)
