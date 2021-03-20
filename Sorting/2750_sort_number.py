def merge_sort(list):
    n = len(list)
    if n == 1:
        return list
    elif n == 2:
        if list[0] > list[1]:
            return list[::-1]
        else:
            return list
    L = merge_sort(list[:n // 2])
    R = merge_sort(list[n // 2:])
    l = len(L)
    r = len(R)
    i = j = 0
    sort_list = []
    while not (i == l and j == r):
        if i == l:
            sort_list.append(R[j])
            j += 1
        elif j == r:
            sort_list.append(L[i])
            i += 1
        elif L[i] < R[j]:
            sort_list.append(L[i])
            i += 1
        else:
            sort_list.append(R[j])
            j += 1
    return sort_list

if __name__ == '__main__':
    N = int(input())
    nums = []
    for i in range(N):
        nums.append(int(input()))
    nums = merge_sort(nums)
    for i in nums:
        print(i)
