def hanoi(n, ans, stack, dest, temp):
    if n == 1:
        ans.append(f'{stack} {dest}')
        return
    hanoi(n - 1, ans, stack, temp, dest)
    ans.append(f'{stack} {dest}')
    hanoi(n - 1, ans, temp, dest, stack)


if __name__ == '__main__':
    N = int(input())
    trace = []
    hanoi(N, trace, 1, 3, 2)
    print(len(trace))
    for s in trace:
        print(s)
