def hanoi(n, l):
    if n == 1:
        l.append(('1 3'))
        return 1


if __name__ == '__main__':
    N = int(input())
    trace = []
    T = hanoi(N, trace)
    print(T)
    for s in trace:
        print(s)
