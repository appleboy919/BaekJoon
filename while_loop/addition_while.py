sum_list = []

k,v = input().split()
k = int(k)
v = int(v)
while (k,v) != (0,0):
    sum_list.append(k+v)
    k,v = input().split()
    k = int(k)
    v = int(v)

for sum in sum_list:
    print(sum)
