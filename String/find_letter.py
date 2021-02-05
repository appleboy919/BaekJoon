import sys

S = input()

for i in range(97, 123):
    try:
        char_index = S.index(chr(i))
    except ValueError:
        char_index = -1
    print(char_index, end=' ')
