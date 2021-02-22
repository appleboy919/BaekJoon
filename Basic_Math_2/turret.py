def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)


def main():
    T = int(input())
    ans = []
    for i in range(T):
        x1, y1, r1, x2, y2, r2 = map(float, input().split())
        p1 = (x1, y1)
        p2 = (x2, y2)
        d = distance(p1, p2)
        if d == 0 and r1 == r2:
            ans.append(-1)
        elif r1+r2 > d and float(abs(r1-r2)) < d:
            # inner circle has to be at least bigger to have two meeting points
            ans.append(2)
        elif r1+r2 == d or r1+d == r2 or r2+d == r1:
            ans.append(1)
        else:
            ans.append(0)
    for i in ans:
        print(i)


if __name__ == '__main__':
    main()
