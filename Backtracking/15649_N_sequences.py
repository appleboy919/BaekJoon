import sys


def print_list(list):
    for i in list:
        sys.stdout.write(str(i) + ' ')
    sys.stdout.write('\n')


def print_sequences(m, n):
    seq = [i for i in range(1, m + 1)]
    last_index = m - 1
    temp_index = 0
    index_flag = False
    while True:
        while seq[last_index] <= n:
            print_list(seq)
            seq[last_index] += 1

        # set variables for backtracking
        seq[last_index] -= 1
        temp_index = last_index - 1

        # backtrack indices
        while temp_index >= 0:
            if seq[temp_index] < seq[temp_index + 1] - 1:
                index_flag = True
                break
            temp_index -= 1

        # find possible cases
        if index_flag:
            while temp_index <= last_index:
                seq[temp_index] += 1
                temp_index += 1
            index_flag = False
        else:
            break


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    print_sequences(M, N)
