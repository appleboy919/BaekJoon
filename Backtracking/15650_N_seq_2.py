import sys


def print_seq(seq):
    for i in seq:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')


def n_sequences(n, m):
    num_used = [True] * n
    seq = []
    for i in range(1, m + 1):
        seq.append(i)
        num_used[i - 1] = False
    track_index = m - 1
    i_flag = False
    while True:
        current = seq[track_index]
        while current <= n:
            # print sequence
            print_seq(seq)

            # increment seq number
            current += 1
            if num_used[current - 1]:
                i_flag = True
                seq[track_index] = current
                break




if __name__ == '__main__':
    N, M = sys.stdin.readline().split()
    n_sequences(N, M)
