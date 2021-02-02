A = int(input())
B = int(input())
C = int(input())

ABC = A*B*C
ABC = str(ABC)

nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in ABC:
    nums[int(i)] += 1

for i in nums:
    print(i)
