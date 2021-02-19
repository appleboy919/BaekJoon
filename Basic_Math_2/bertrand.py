def bertrand(n):
    eratos = [True] * (2*n+1)
    x = int((2*n)**(1/2))
    for i in range(2, x+1):
        if eratos[i]:
            for j in range(i**2, 2*n+1, i):
                eratos[j] = False
    return len([i for i in range(n+1, 2*n+1) if eratos[i]])


def main():
    ans_list = []
    while True:
        n = int(input())
        if n == 0:
            break
        ans_list.append(bertrand(n))

    for i in ans_list:
        print(i)


if __name__ == '__main__':
    main()
