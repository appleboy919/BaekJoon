def body_grades(l, a):
    n = len(l)
    for i in range(n):
        for j in range(n):
            if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
                a[i] += 1


if __name__ == '__main__':
    N = int(input())
    l = []
    a = [1] * N
    for i in range(N):
        l.append(tuple(map(int, input().split())))
    body_grades(l, a)
    for i in a:
        print(i, end=' ')
    print()

    # use sys.stdout for output
