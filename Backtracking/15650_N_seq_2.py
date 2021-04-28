import sys


def print_seq(seq):
    for i in seq:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')


def n_sequences(n, m):
    seq = [i for i in range(1, m+1)]
    rep_flag = True
    while rep_flag:
        track_index = m-1
        current = seq[track_index]
        while current <= n:
            seq[track_index] = current
            print_seq(seq)
            current += 1
        rep_flag = False
        track_index -= 1
        while track_index >= 0:
            if seq[track_index] < n-(m-1-track_index):
                seq[track_index] += 1
                while track_index < m-1:
                    track_index += 1
                    seq[track_index] = seq[track_index-1] + 1
                    rep_flag = True
                break
            track_index -= 1
      


if __name__ == '__main__':
  N, M = map(int, sys.stdin.readline().split())
  n_sequences(N, M)
