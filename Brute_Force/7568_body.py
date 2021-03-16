def body_grades(l, a):
    length = len(l)
    temp = []
    grade = 1
    max_index = 0
    max_data = None

    while grade <= length:
        # initialize max_data and temp list before getting into inner loop
        max_data = None
        temp = []
        # start inner loop for biggest body data from the rest
        for i in range(length):
            if not a[i]:
                if max_data:
                    if max_data[0] < l[i][0] and max_data[1] < l[i][1]:
                        max_data = l[i]
                        max_index = i
                        temp.clear()
                    elif max_data[0] > l[i][0] and max_data[1] > l[i][1]:
                        pass
                    else:
                        temp.append(i)
                else:
                    max_data = l[i]
                    max_index = i

        if temp:  # if there are ties in the data
            temp.append(max_index)
            for j in temp:
                a[j] = grade
            grade += len(temp)
        else:  # no ties
            a[max_index] = grade
            grade += 1


if __name__ == '__main__':
    N = int(input())
    l = []
    a = [0] * N
    for i in range(N):
        l.append(tuple(map(int, input().split())))
    body_grades(l, a)
    for i in a:
        print(i, end=' ')
    print()
