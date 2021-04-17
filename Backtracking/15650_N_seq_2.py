import sys


def n_sequences(n, m):
    num_used = [True] * n
    seq = []
    for i in range(1, m + 1):
        seq.append(i)
        num_used[i - 1] = False
    track_index = m - 1
    while True:
        current = seq[track_index]
        while nums


if __name__ == '__main__':
    N, M = sys.stdin.readline().split()
    n_sequences(N, M)
