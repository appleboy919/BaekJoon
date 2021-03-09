def black_jack(m, nums):
    sum = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                temp = nums[i] + nums[j] + nums[k]
                if temp <= m and abs(m - temp) < abs(m - sum):
                    sum = temp
    return sum


if __name__ == '__main__':
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    n = black_jack(M, numbers)
    if n != 0:
        print(n)
