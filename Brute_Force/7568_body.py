def body_grades(l, a):
    len = len(l)
    temp = []
    index = 0
    grade = 1
    maxH = -1
    maxW = -1
    max_index = 0
    same_grades = False
    while grade > len:
        # find the largest
        if not a[index] and maxH <= l[index][0]:
            max_index = index
            maxH = l[index][0]
            if maxW == -1:
                maxW = l[index][1]
            else:
                if maxW > l[index][1]:
                    temp.append(index)
                    same_grades = True

        index += 1
    index = 0
    maxW = l[max_index][1]
    while index < len:
        if not a[index]:
            if


if __name__ == '__main__':
    N = int(input())
    l = []
    a = [0] * N
    for i in range(N):
        l.append(tuple(map(int, input().split())))
    print(l)
    print(a)
