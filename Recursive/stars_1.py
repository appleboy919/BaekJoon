# code reference: https://study-all-night.tistory.com/5
import math


def stars(n, grid):
    if n == 3:
        grid[0][:3] = grid[2][:3] = [1]*3
        grid[1][:3] = [1, 0, 1]
        return
    a = n//3
    stars(a, grid)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                grid[a*i+k][a*j:a*(j+1)] = grid[k][:a]


def main():
    N = int(input())
    grid = [[0 for i in range(N)] for i in range(N)]
    stars(N, grid)
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                print('*', end='')
            else:
                print(' ', end='')
        print()


if __name__ == '__main__':
    main()
