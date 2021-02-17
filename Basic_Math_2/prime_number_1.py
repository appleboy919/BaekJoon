N = int(input())
nums = list(map(int, input().split()))
prime_nums = 0
for i in nums:
    is_primeNum = True
    if i == 1:
        continue
    for j in range(1, i):
        if j != 1 and i % j == 0:
            is_primeNum = False
            break
    if is_primeNum:
        prime_nums += 1
print(prime_nums)
