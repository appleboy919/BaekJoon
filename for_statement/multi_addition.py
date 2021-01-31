T = int(input())
sum = []

for i in range(0, T):
    a, b = input().split()
    a = int(a)
    b = int(b)
    sum.append(a+b)

for k in sum:
    print(k)
