import sys


def print_seq(seq):
    for i in seq:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')


def n_sequences(n, m):
    seq = [i for i in range(1, m+1)]

    while True:
        track_index = m-1
        current = seq[track_index]
        while current <= n:
            seq[track_index] = current
            print_seq(seq)
            current += 1




if __name__ == '__main__':
    N, M = sys.stdin.readline().split()
    n_sequences(N, M)
