import sys
import time

ans = 0


# check the current position
def check_pos(cols, row, col):
    col_num = 0
    init_row = row
    while row > 0:
        row -= 1
        if abs(init_row - row) == abs(cols[row] - col):
            return False
    return True


def n_queen(n, cols, row, emp_cols):
    for i in emp_cols:
        if check_pos(cols, row, i):
            if row == n - 1:
                global ans
                ans += 1
            else:
                cols[row] = i
                temp_cols = cols[:]
                temp_emp = [k for k in emp_cols if k != i]
                n_queen(n, temp_cols, row + 1, temp_emp)


temp = time.time()
N = int(sys.stdin.readline())
n_queen(N, [-1] * N, 0, [i for i in range(N)])
print(f'total time: {time.time() - temp}')
sys.stdout.write(str(ans))
