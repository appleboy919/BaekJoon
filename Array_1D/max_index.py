nums = []
for i in range(9):
    nums.append(int(input()))

max = 0
index = 1
ret_index = 0 

for i in nums:
    if max < i:
        max = i
        ret_index = index
    index+=1

print(max)
print(ret_index)