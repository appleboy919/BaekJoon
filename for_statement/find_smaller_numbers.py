N, X = input().split()
N = int(N)
X = int(X)
ints = input().split()
ints = list(map(int, ints))

for i in ints:
    if i < X:
        print(i, end=' ')
print('')
