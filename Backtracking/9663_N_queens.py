import sys

# check the current position
def check_pos(n, cols, row, col):
    col_num = 0
    while row > 0:
        row -= 1
        col_num += 1
        if cols[row] == col:
            return False
        if col - col_num >= 0 and cols[row] == col - col_num:
            return False
        if col - col_num < n and cols[row] == col + col_num:
            return False
    return True


def N_queens(n):
    colPos = [-1] * n
    row = 0
    ans = 0

    # start the outer loop
    while True:

        # check each cell in the current row
        for i in range(n):
            if check_pos(n, colPos, row, i):
                # n-th queen has been placed --> +1
                if row == n - 1:
                    ans += 1
                    continue
                colPos[row] = i
                break

        # backtrack starts here
        if colPos[row] == -1:
            end_bt = False
            while row > 0 and not end_bt:
                row -= 1
                for i in range(colPos[row] + 1, n):
                    if check_pos(n, colPos, row, i):
                        end_bt = True
                        colPos[row] = i
                        break
                if not end_bt:
                    colPos[row] = -1
            if not end_bt and row == 0:
                break
        row += 1
    return ans


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    sys.stdout.write(str(N_queens(N)))
