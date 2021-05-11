import sys


def mark_col(board, row, col, n):
    while row <= n - 1:
        board[row][col] = False
        row += 1


def marK_diagonal(board, row, col, n):
    while row < n and col < n:
        board[row][col] = False
        row += 1
        col += 1


def print_N_queens(n):
    board = [[True] * n] * n
    ans = 0
    init_col = 0
    # TODO: check diagonal??
    row = 0

    # start the outer loop
    while True:
        # initial position of q on (1,1)
        board[row][init_col] = False

        # mark diagonal, row to False
        mark_col(board, row, init_col, n)
        marK_diagonal(board, row, init_col, n)

        # start the first inner loop for positioning queens on each row
        while row < n:
            row += 1
            for col in range(n):
                if board[row][col]:
                    if row == n - 1:
                        ans += 1
                        continue
                    mark_col(board, row, col, n)
                    marK_diagonal(board, row, col, n)
                    break


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    print_N_queens(N)
