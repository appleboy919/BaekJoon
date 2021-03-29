import sys


def comp_words(w1, w2):
    if len(w1) < len(w2):
        return True
    elif len(w1) == len(w2):
        return w1 < w2
    return False


def mergeSort_words(list, n):
    if n == 1:
        return list
    L = mergeSort_words(list[:n // 2], n // 2)
    R = mergeSort_words(list[n // 2:], n - n // 2)
    l = r = 0
    temp = []
    while not (l == n // 2 and r == n - n // 2):
        if l == n // 2:
            temp.append(R[r])
            r += 1
        elif r == n - n // 2:
            temp.append(L[l])
            l += 1
        elif comp_words(L[l], R[r]):
            temp.append(L[l])
            l += 1
        else:
            temp.append(R[r])
            r += 1
    return temp


def sort_words(n):
    temp = []
    for i in range(n):
        temp.append(sys.stdin.readline().rstrip())
    temp = mergeSort_words(temp, n)
    words = []
    i = 0
    index = 0
    while i < n:
        if i == 0:
            words.append(temp[i])
            index += 1
        else:
            if temp[i] != words[index - 1]:
                words.append(temp[i])
                index += 1
        i += 1
    for w in words:
        sys.stdout.write(w + '\n')


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    sort_words(N)
