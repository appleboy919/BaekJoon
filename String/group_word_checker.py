N = int(input())

num = 0

for i in range(N):
    letters = []
    is_gw = True
    word = input()
    prv_letter = ''
    for c in word:
        if c != prv_letter:
            if c in letters:
                # print(f'{c} makes {word} not a GW!')
                is_gw = False
                break
            prv_letter = c
            letters.append(c)
    if is_gw:
        num += 1

print(num)
