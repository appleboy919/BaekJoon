def how_many_kg(n):
    if n % 5 == 0:
        return n//5
    for i in range(1, 5):
        if n-3*i >= 0 and (n-3*i) % 5 == 0:
            return (n-3*i)//5 + i
    return -1

N = int(input())
print(how_many_kg(N))

# For testing
# while True:
#     N = int(input())
#     print(how_many_kg(N))
