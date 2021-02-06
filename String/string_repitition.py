N = int(input())
strings = []

for i in range(N):
    s = input()
    temp_string = ''
    for c in s:
        temp_string += c*3
    strings.append(temp_string)

index = 1
for new_string in strings:
    print(index, end=' ')
    print(new_string)
    index += 1
