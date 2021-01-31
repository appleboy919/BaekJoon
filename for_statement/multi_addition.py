T = int(input())
sum = []

for i in range(0, T):
    a, b = input().split()
    a = int(a)
    b = int(b)
    sum.append(a+b)

i = 1
for k in sum:
    print('Case #{}: {}'.format(i, k))
    i += 1
