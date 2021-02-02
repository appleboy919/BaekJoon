N = int(input())
if N == 1:
    integers = [int(input())]
else:
    integers = input().split()
    integers = list(map(int, integers))

max = -1000000
min = 1000000

for i in integers:
    max = i if i > max else max
    min = i if i < min else min

print(min, max)

# integers = map(int, input())
