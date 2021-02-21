def last_point(points):
    i = 0
    x = dict()
    y = dict()
    ans = []
    while i < 3:
        if points[i][0] not in x:
            x[points[i][0]] = 0
        if points[i][1] not in y:
            y[points[i][1]] = 0
        x[points[i][0]] += 1
        y[points[i][1]] += 1
        i += 1
    for i in x.keys():
        if x[i] == 1:
            ans.append(i)
    for j in y.keys():
        if y[j] == 1:
            ans.append(j)
    return ans


def main():
    points = []
    for i in range(3):
        points.append(tuple(map(int, input().split())))
    point = last_point(points)
    print(f'{point[0]} {point[1]}')


if __name__ == '__main__':
    main()
