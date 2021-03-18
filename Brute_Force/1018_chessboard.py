def min_replacement(l, N, M):
    ans = 50*50
    for i in range(N-7):
        for j in range(M-7):
            rep_num = 0
            if l[i][j] == 'B':
                is_black = 1
            else:
                is_black = -1
            for row in range(i, i+8):
                for col in range(j, j+8):
                    if is_black == 1:
                        if l[row][col] == 'W':
                            rep_num += 1
                    else:
                        if l[row][col] == 'B':
                            rep_num += 1
                    is_black *= -1
                is_black *= -1
            if ans > rep_num:
                ans = rep_num
    return ans




if __name__ == '__main__':
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        board.append(input())
    print(min_replacement(board, N, M))