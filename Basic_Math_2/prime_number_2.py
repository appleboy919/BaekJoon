def primeNumber(a, b):
    min = -1
    sum = 0
    for i in range(a, b+1):
        is_primeNum = True
        if i == 1:
            continue
        for j in range(1, i):
            if j != 1 and i % j == 0:
                is_primeNum = False
                break
        if is_primeNum:
            if min == -1:
                min = i
            sum += i
    return (sum, min)


def main():
    M = int(input())
    N = int(input())
    ans = primeNumber(M, N)
    for i in ans:
        if i == 0:
            continue
        print(i)


if __name__ == '__main__':
    main()
