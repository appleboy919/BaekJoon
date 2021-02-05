import sys

N = int(input())
s = sys.stdin.readline().rstrip()
sum = 0
for i in range(N):
    sum += int(s[i])
print(sum)
