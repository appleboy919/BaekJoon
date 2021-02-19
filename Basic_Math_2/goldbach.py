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


def main():
    T = int(input())
    inputs = []
    for i in range(T):
        inputs.append(int(input()))
    primeNums = eratos_primenums(max(inputs))
    for i in inputs:
        print(goldbach(primeNums, i))


if __name__ == '__main__':
    main()
