def goldbach(n):
    eratos = [True] * (n+1)
    x = int(n**(1/2))
    for i in range(2, x+1):
        if eratos[i]:
            for j in range(i**2, n+1, i):
                eratos[j] = False
    primeNums = [i for i in range(2, n) if eratos[i]]
    temp = []
    for i in primeNums:
        if n-i < i:
            break
        if n-i in primeNums:
            temp.insert(0, (i, n-i))
    return f'{temp[0][0]} {temp[0][1]}'


def main():
    T = int(input())
    ans_list = []
    for i in range(T):
        n = int(input())
        ans_list.append(goldbach(n))
    for s in ans_list:
        print(s)


if __name__ == '__main__':
    main()
