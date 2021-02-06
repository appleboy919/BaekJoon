def dial_time(c):
    if ord(c) < 83:
        dial_number = (ord(c)+1)//3-20
    elif ord(c) == 83:
        dial_number = 7
    elif ord(c) <= 86:
        dial_number = 8
    else:
        dial_number = 9
    return dial_number + 1


N = input()
time = 0
for n in N:
    time += dial_time(n)
print(time)
