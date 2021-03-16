def body_grades(l, a):
    # group each data with same tier
    temp = []
    jump = False
    for i in range(len(l)):
        jump = False
        if not temp:
            temp.append([i])
        else:
            # TODO: the problem is here!! (order of grouping)
            for same_grade in temp:
                for data in same_grade:
                    if l[data][0] > l[i][0] and l[data][1] > l[i][1]:
                        pass
                    elif l[data][0] < l[i][0] and l[data][1] < l[i][1]:
                        pass
                    else:
                        same_grade.append(i)
                        jump = True
                        break
                if jump:
                    break
            if not jump:
                temp.append([i])

    # grade each group of data
    grade = 1
    grades = []
    for i in range(len(temp)):
        grades.append((l[temp[i][0]][0], i))
    grades = sorted(grades, reverse=True)
    for g in grades:
        for k in temp[g[1]]:
            a[k] = grade
        grade += len(temp[g[1]])
    print('Done!')


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
