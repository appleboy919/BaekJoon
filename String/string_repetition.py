N = int(input())
strings = []

for i in range(N):
    n, s = input().split()
    n = int(n)
    temp_string = ''
    for c in s:
        temp_string += c*n
    strings.append(temp_string)

for new_string in strings:
    print(new_string)
