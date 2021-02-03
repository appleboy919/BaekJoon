def d(n):
    number = n
    for i in str(n):
        number += int(i)
    return number


self_nums = set(range(1, 10001))

for i in range(1, 10000):
    try:
        self_nums.remove(d(i))
    except KeyError:
        pass

for i in self_nums:
    print(i)
