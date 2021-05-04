import sys


def print_list(l):
    for i in l:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')


def print_seq(m, n):
    seq = [1] * m
    index = m - 1
    loop_flag = True
    while loop_flag:
        while seq[index] <= n:
            print_list(seq)
            seq[index] += 1
        loop_flag = False
        while index > 0:
            index -= 1
            if seq[index] < n:
                seq[index] += 1
                while index < m - 1:
                    prv = seq[index]
                    index += 1
                    seq[index] = prv
                loop_flag = True
                break


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    print_seq(M, N)
