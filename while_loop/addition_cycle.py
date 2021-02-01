N = input()
if len(N) == 1:
    N = '0' + N
new_N = N
cycle = 0
while True:
    if len(new_N) == 1:
        new_N = '0' + new_N
    x = int(new_N[0])+int(new_N[1])
    new_N = new_N[1]+str((x % 10))
    cycle += 1
    if N == new_N:
        break

print(cycle)
