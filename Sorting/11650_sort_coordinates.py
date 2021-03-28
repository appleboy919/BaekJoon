import sys


def merge_sort(list, n):
    if n == 1:
        return list
    L = merge_sort(list[:n // 2], n // 2)
    R = merge_sort(list[n // 2:], n - n // 2)
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
        elif L[l] < R[r]:
            temp.append(L[l])
            l += 1
        else:
            temp.append(R[r])
            r += 1
    return temp


def print_sorted_coordinates(n):
    coordinates = []
    for i in range(n):
        coordinates.append(tuple(map(int, sys.stdin.readline().split())))
    coordinates = merge_sort(coordinates, n)
    for c in coordinates:
        sys.stdout.write(str(c[0]) + ' ' + str(c[1]) + '\n')


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    print_sorted_coordinates(N)
