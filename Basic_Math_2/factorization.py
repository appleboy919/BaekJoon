import math


def next_primeNum(n):
    num = n
    while True:
        num += 1
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            return num


def factorization(n):
    fact_list = []
    p = 2
    loop = 1
    while True:
        loop += 1
        if n % p == 0:
            n /= p
            fact_list.append(p)
            if n == 1:
                break
            continue
        p = next_primeNum(p)
    print(f'loop iteration: {loop}')
    return fact_list


# This is a faster algorithm which checks the integer with i (1<i<sqrt(n)) for its factors
def fast_factor(n):
    fact_list = []
    x = int(math.sqrt(n))
    i = 2
    while i <= x:
        if n == 1:
            return fact_list
        if n % i == 0:
            fact_list.append(i)
            n //= i
            i -= 1
        i += 1
    fact_list.append(n)
    return fact_list


"""
def factorization(n):
    temp = [2]
    fact_list = []
    p = 2
    while True:
        if n % p == 0:
            n /= p
            fact_list.append(p)
            if n == 1:
                break
            continue
        while True:
            p += 1
            is_prime = True
            for i in temp:
                if p % i == 0:
                    is_prime = False
                    break
            if is_prime:
                temp.append(p)
                break
    return fact_list
"""


def main():
    N = int(input())
    if N == 1:
        exit()
    fact_nums = fast_factor(N)
    for i in fact_nums:
        print(i)


if __name__ == '__main__':
    main()
