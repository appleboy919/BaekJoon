import sys
def print_list(list):
    for i in list:
        sys.stdout.write(str(i)+' ')
    sys.stdout.write('\n')

def print_sequences(n, m):
    indices = [i for i in range(1, n)]
    last_index = n
    while True:
        print_list(indices.extend([last_index]))

    len_index = 0
if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    print_sequences(N, M)