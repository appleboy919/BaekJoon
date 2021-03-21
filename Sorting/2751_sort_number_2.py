import sys

if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        l.append(int(sys.stdin.readline()))
    for i in sorted(l):
        sys.stdout.write(f'{i}' + '\n')
