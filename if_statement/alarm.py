a, b = input().split()

h = int(a)
m = int(b)

if m-45 < 0:
    if h-1 < 0:
        h = 23
    else:
        h = h-1
    m = m+15
else:
    m = m-45
print(h, m)
