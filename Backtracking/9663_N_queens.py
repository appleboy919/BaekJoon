import sys
import time


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


def N_queens(n):
    colPos = [-1] * n
    temp_col = [i for i in range(n)]
    row = 0
    ans = 0
    total_time = time.time()
    bt_time = 0
    # start the outer loop
    while True:

        # check each cell in the current row
        for i in temp_col:
            if check_pos(n, colPos, row, i):
                # n-th queen has been placed --> +1
                if row == n - 1:
                    ans += 1
                    continue
                colPos[row] = i
                temp_col.remove(i)
                break
        temp = time.time()
        # backtrack starts here
        if colPos[row] == -1:
            end_bt = False
            while row > 0 and not end_bt:
                row -= 1
                for i in [i for i in temp_col if i > colPos[row]]:
                    if check_pos(n, colPos, row, i):
                        end_bt = True
                        temp_col.append(colPos[row])
                        temp_col.sort()
                        colPos[row] = i
                        temp_col.remove(i)
                        break
                if not end_bt:
                    temp_col.append(colPos[row])
                    temp_col.sort()
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
