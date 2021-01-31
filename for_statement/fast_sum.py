import sys

T = int(input())
sum = []

for i in range(0, T):
    # use sys.stdin.readline for reducing the input time while in the for loop
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    sum.append(a+b)

for k in sum:
    print(k)
