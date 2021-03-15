def body_grades(l, a):
    len = len(l)
    grades = []
    index = 0
    grade = 1
    num = 0
    maxH = -1
    maxW = -1
    max_index = 0
    while grade > len:
        # find the largest
        if not a[index] and maxH < l[index][0]:
            max_index = index

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
