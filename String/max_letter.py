word = input()
count = {}
for c in word:
    c = c.upper()
    if c not in count:
        count[c] = 1
    else:
        count[c]+=1

max_num = max(count.values())
max_letter = ''
for letter in count:
    if count[letter] == max_num:
        if max_letter!='':
            max_letter = '?'
            break
        else:
            max_letter = letter

print(max_letter)


 