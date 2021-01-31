# 1
n = int(input())

for i in range(1, n+1):
    for k in range(1, i+1):
        print('*', end='')
    print('')

# 2
n = int(input())

for i in range(1, n+1):
    for k in range(1, n+1-i):
        print(' ', end='')
    for j in range(n+1-i, n+1):
        print('*', end='')
    print('')
