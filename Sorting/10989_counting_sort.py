import sys


def count_sort(N):
    counts = [0] * 10001

    # count each numbers
    i = 0
    while i < N:
        counts[int(sys.stdin.readline())] += 1
        i += 1

    # modify count array to store sum of each previous counts
    index = 0
    while index < 10001:
        counts[index] += counts[index - 1]
        index += 1

    ans = []
    # print each numbers from the counts
    count = 0
    i = 0
    while i < 10001:
        counts[i] -= count
        while counts[i] != 0:
            ans.append(i)
            count += 1
            counts[i] -= 1
        i += 1
    return ans


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    sorted_list = count_sort(N)
    for i in sorted_list:
        sys.stdout.write(f'{i}' + '\n')
