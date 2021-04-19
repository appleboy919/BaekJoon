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
    while True:
        # print sequence
        print_seq(seq)

        # increment seq number
        while True:
            i_flag = False
            current = seq[track_index]
            while current <= n:
                current += 1
                if num_used[current - 1]:
                    i_flag = True
                    num_used[seq[track_index] - 1] = True
                    num_used[current - 1] = False
                    seq[track_index] = current
                    break
            if not i_flag:  # need back tracking
                while track_index <= m - 1:
                    track_index -= 1


if __name__ == '__main__':
    N, M = sys.stdin.readline().split()
    n_sequences(N, M)
