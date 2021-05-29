import sys
import time

ans = 0


# check the current position
def check_pos(n, cols, row, col):
    col_num = 0
    while row > 0:
        row -= 1
        col_num += 1
        if col - col_num >= 0 and cols[row] == col - col_num:
            return False
        if col - col_num < n and cols[row] == col + col_num:
            return False
    return True


def n_queen(n, cols, row):
    for i in [i for i in range(n) if i not in cols]:
        if check_pos(n, cols, row, i):
            if row == n - 1:
                global ans
                ans += 1
            else:
                cols[row] = i
                temp_cols = cols[:]
                n_queen(n, temp_cols, row + 1)


temp = time.time()
n = int(sys.stdin.readline())
n_queen(n, [-1] * n, 0)
print(f'total time: {time.time() - temp}')
sys.stdout.write(str(ans))
