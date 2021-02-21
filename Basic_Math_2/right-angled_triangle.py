def is_right_angled(sides):
    max_side = max(sides)
    sum = 0
    for i in sides:
        if i != max_side:
            sum += i**2
    if sum != max_side**2:
        return 'wrong'
    return 'right'


def main():
    ans = []
    while True:
        temp = list(map(int, input().split()))
        if temp[0]+temp[1]+temp[2] == 0:
            break
        ans.append(is_right_angled(temp))
    for s in ans:
        print(s)


if __name__ == '__main__':
    main()
