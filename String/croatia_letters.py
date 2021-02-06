S = input()
letters = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
temp_len = len(S)
total = 0
for l in letters:
    num = S.count(l)
    # print(f'{l}: {num}')
    temp_len -= num * len(l)
    total += num
# print(f'temp_len: {temp_len}')
total += temp_len + S.count('dz=')
print(total)
