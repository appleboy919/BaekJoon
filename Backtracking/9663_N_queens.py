import sys


def mark_pos(n, board, row, col, check):
    # check cells on same column
    for i in range(row + 1, n):
        board[i][col] = check

    # check diagonal cells
    while row < n and col < n:
        board[row][col] = check
        row += 1
        col += 1


def N_queens(n):
    colPos = [0] * n
    board = [[True] * n] * n
    row = col = 0
    ans = 0
    while True:
        for i in range(n):
            if board[row][i]:
                if row == n - 1:
                    # test
                    print('+1 at', str(row), str(col))
                    ans += 1
                    continue
                colPos[row] = i
                mark_pos(n, board, row, i, False)
                break

        # backtrack starts here
        if row == n - 1:
            end_bt = False
            while row >= 0 and not end_bt:
                row -= 1
                for i in range(colPos[row], n):
                    if board[row][i]:
                        end_bt = True
                        colPos[row] = i
                        mark_pos(n, board, row, col, False)
                        break
                if not end_bt:
                    mark_pos(n, board, row, colPos[row], True)
            if not end_bt and row == 0:
                break
        row += 1


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    sys.stdout.write(str(N_queens(N)))
