def arith_mean(nums, n):
    print(f'{round(sum(nums)/n)}')

def middle(nums, n):
    print(f'{sorted(nums)[n//2]}')

def frequent(nums, n):


if __name__ == '__main__':
    N = int(input())
    nums = []
    for i in range(N):
        nums.append(int(input()))