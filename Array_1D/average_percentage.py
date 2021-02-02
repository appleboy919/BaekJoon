import sys

C = int(input())
for i in range(C):
    case = list(map(int, sys.stdin.readline().split()))
    avg = sum(case[1:])/case[0]
    n = 0
    for j in case[1:]:
        if j > avg:
            n += 1
    print('%.3f%%' % (n/case[0]*100))
