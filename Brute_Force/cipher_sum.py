def get_sum(n):
    num_string = str(n)
    sum = n
    for i in range(len(num_string)):
        sum += int(num_string[i])
    return sum


def min_gen(n):
    if n < 10:
        return n // 2 if n % 2 == 0 else 0
    else:
        num_string = str(n)
        temp = int('9'*(len(num_string)-1))
        for i in range(n-temp,n):
            x = get_sum(i)
            print(f'{i} -> {x}')
            if x==n:
                return i
        return 0


if __name__ == '__main__':
    while True:
        N = int(input())
        print(min_gen(N))
