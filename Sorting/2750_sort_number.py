def merge_sort(list):


if __name__ == '__main__':
    N = int(input())
    nums = []
    for i in range(N):
        nums.append(int(input()))
    nums = merge_sort(nums)
    for i in nums:
        print(i)