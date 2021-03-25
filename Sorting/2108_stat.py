def arith_mean(nums, n):
    return round(sum(nums) / n)


def middle_and_range(nums, n):
    sort_nums = sorted(nums)
    return sort_nums[n // 2], sort_nums[n - 1] - sort_nums[0]


def frequent(nums, n):
    temp = [0] * 8001
    max_num = 0
    max_vals = []
    for i in nums:
        temp[i + 4000] += 1
        if max_num < temp[i + 4000]:
            max_num = temp[i + 4000]
            max_vals.clear()
            max_vals.append(i)
        elif max_num == temp[i + 4000]:
            max_vals.append(i)
    ans = max_vals[0] if len(max_vals) == 1 else sorted(max_vals)[1]
    return ans


if __name__ == '__main__':
    N = int(input())
    nums = []
    for i in range(N):
        nums.append(int(input()))
    mid_range = middle_and_range(nums, N)
    print(arith_mean(nums, N))
    print(mid_range[0])
    print(frequent(nums, N))
    print(mid_range[1])
