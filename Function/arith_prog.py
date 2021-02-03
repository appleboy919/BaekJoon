N = int(input())

num = 0
for i in range(1, N+1):
    is_num = True
    if i < 100:
        num += 1
    else:
        nums = list(map(int, str(i)))
        common_diff = nums[0] - nums[1]
        for j in range(1, len(nums)-1):
            if nums[j] - nums[j+1] != common_diff:
                is_num = False
                break
        if is_num:
            num += 1

print(num)
