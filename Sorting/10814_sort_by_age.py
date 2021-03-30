import sys


def merge_sort(list, n):
    if n == 1:
        return list
    L = merge_sort(list[:n // 2], n // 2)
    R = merge_sort(list[n // 2:], n - n // 2)
    i = 0
    l = r = 0
    temp = []
    while not (l == n // 2 and r == n - n // 2):
        if l == n // 2:
            temp.append(R[r])
            r += 1
        elif r == n - n // 2:
            temp.append(L[l])
            l += 1
        elif L[l][0] <= R[r][0]:
            temp.append(L[l])
            l += 1
        else:
            temp.append(R[r])
            r += 1
    return temp


def age_sort(n):
    name_age = []
    for i in range(n):
        name_age.append(tuple(sys.stdin.readline().split()))
    name_age = merge_sort(name_age, n)
    for t in name_age:
        sys.stdout.write(t[0] + ' ' + t[1] + '\n')


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    age_sort(N)
