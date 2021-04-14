import sys


def coord_compress(list):
    coord = []
    index = 0
    for i in list:
        coord.append((i, index))
        index += 1
    coord.sort()
    num = 0
    prv = coord[0][0]
    for t in coord:
        if t[0] != prv:
            num += 1
        list[t[1]] = num
        prv = t[0]
    return list


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    Xs = list(map(int, sys.stdin.readline().split()))
    Xs = coord_compress(Xs)
    for i in Xs:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')
