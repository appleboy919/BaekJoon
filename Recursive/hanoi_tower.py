def hanoi(n, l, N):
    if n == 1:
        if N % 2 == 0:
            l.append('1 2')
        else:
            l.append('1 3')
        return
    hanoi(n - 1, l, N)
    if l[len(l) - 1][2] == '3':
        l.append('1 2')

    else:
        l.append('1 3')


## n%2 == 0: 1->2


if __name__ == '__main__':
    N = int(input())
    trace = []
    hanoi(N, trace, N)
    print(len(trace))
    for s in trace:
        print(s)
