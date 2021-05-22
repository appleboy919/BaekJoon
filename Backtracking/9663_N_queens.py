import sys
import time


# check the current position
# TODO: try to save the diagonal state rather than running each function
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
    total_time = time.time()
    bt_time = 0
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
        temp = time.time()
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
        bt_time = bt_time + (time.time() - temp)
        row += 1
    total_time = time.time() - total_time
    print('total time:', total_time)
    print('backtrack time:', bt_time)
    return ans


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    sys.stdout.write(str(N_queens(N)))
