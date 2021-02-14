# reference: https://ooyoung.tistory.com/89


# DO NOT USE THIS FUNCTION
def f(k, n):
    if k == 0:
        return n
    return f(k-1, n)+f(k, n-1)


T = int(input())
ans_list = []
for i in range(T):
    k = int(input())
    n = int(input())
    f = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            f[j] += f[j-1]
    ans_list.append(f[n-1])

for i in ans_list:
    print(i)

# The idea is to get a list of numbers in a given floor by adding up from 2nd room,
# previous i-th room number + (i-1)th room on the same floor. This is possible since
# the 1st room on each floor has only 1 numbers.
