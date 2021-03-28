import sys


def comp_cords(p1, p2):
    if p1[1] > p2[1]:
        return 0
    elif p1[1] == p2[1]:
        if p1[0] > p2[0]:
            return 0
    return 1


def merge_sort2(list, n):
    if n == 1:
        return list
    L = merge_sort2(list[:n // 2], n // 2)
    R = merge_sort2(list[n // 2:], n - n // 2)
    temp = []
    l = 0
    r = 0
    while not (l == n // 2 and r == n - n // 2):
        if l == n // 2:
            temp.append(R[r])
            r += 1
        elif r == n - n // 2:
            temp.append(L[l])
            l += 1
        elif comp_cords(L[l], R[r]):
            temp.append(L[l])
            l += 1
        else:
            temp.append(R[r])
            r += 1
    return temp


def print_sorted_cords(n):
    cords = []
    for i in range(n):
        cords.append(tuple(map(int, sys.stdin.readline().split())))
    cords = merge_sort2(cords, n)
    for c in cords:
        sys.stdout.write(str(c[0]) + ' ' + str(c[1]) + '\n')

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    print_sorted_cords(N)
