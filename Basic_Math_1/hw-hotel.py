import sys
T = int(input())
ans_list = []
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    f = N % H
    n = f*100+N//H+1 if f != 0 else H*100 + N//H
    ans_list.append(n)
for n in ans_list:
    print(n)
