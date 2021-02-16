# Try this again (BaekJoon-1011)

import math


def max_num(l):
    x = math.ceil(math.sqrt(l))
    if l <= x*(x-1):
        return 2*x-2
    else:
        return 2*x-1


def main():
    n = int(input())
    ans_list = []
    for i in range(n):
        a, b = map(int, input().split())
        ans_list.append(max_num(b-a))
    for i in ans_list:
        print(i)

    # For testing

    # for i in range(1, 21):
    #     print(f'{i}: {max_num(i)}')


if __name__ == "__main__":
    main()
