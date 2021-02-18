# Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import math


def eratos(m, n):
    temp_list = [True] * (n+1)
    x = int(math.sqrt(n))
    for i in range(2, x+1):
        if temp_list[i]:
            for j in range(2*i, n+1, i):
                temp_list[j] = False
    return [i for i in range(m, n+1) if i != 1 and temp_list[i]]


def main():
    M, N = map(int, input().split())
    primeNums = eratos(M, N)
    for i in primeNums:
        print(i)


if __name__ == '__main__':
    main()
