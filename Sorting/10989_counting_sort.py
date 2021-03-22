import sys


def count_sort(nums):
    counts = list(range(10001))

    # count each numbers
    for i in nums:
        counts[i] += 1

    # modify count array to store sum of each previous counts
    for i in range(10001):
        counts[i] += counts[i - 1]

    ans = []
    # print each numbers from the counts
    count = 0
    for i in range(10001):
        counts[i] -= count
        while counts[i] != 0:
            ans.append(i)
            count += 1
            counts[i] -= 1
    return ans


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    l = []
    for i in range(N):
        l.append(int(sys.stdin.readline()))
    sorted_l = count_sort(l)
    for i in sorted_l:
        sys.stdout.write(f'{i}' + '\n')
