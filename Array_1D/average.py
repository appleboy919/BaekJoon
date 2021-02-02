import sys

N = int(input())
scores = list(map(int, sys.stdin.readline().split()))
max = max(scores)
for i in range(N):
    scores[i] = scores[i]/max*100
avg = sum(scores)/N
print(avg)
