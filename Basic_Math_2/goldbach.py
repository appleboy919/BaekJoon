def eratos_primenums(n):
    eratos = [True] * (n+1)
    x = int(n**(1/2))
    for i in range(2, x+1):
        if eratos[i]:
            for j in range(i**2, n+1, i):
                eratos[j] = False
    return [i for i in range(2, n) if eratos[i]]


def goldbach(primeNums, n):
    temp = []
    for i in primeNums:
        if n-i < i:
            break
        if n-i in primeNums:
            temp.insert(0, (i, n-i))
    return f'{temp[0][0]} {temp[0][1]}'


def is_primeNum(n):
    x = int(n**(1/2))
    for i in range(2, x+1):
        if n % i == 0:
            return False
    return True


# faster algorithm to get each goldbach's pair from half
def fast_goldbach(n):
    half = n//2
    for i in range(half, 1, -1):
        if is_primeNum(i) and is_primeNum(n-i):
            return(i, n-i)


def main():
    T = int(input())
    ans = []
    for i in range(T):
        ans.append(fast_goldbach(int(input())))
    for t in ans:
        print(f'{t[0]} {t[1]}')


if __name__ == '__main__':
    main()
