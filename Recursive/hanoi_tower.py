# def hanoi(n, l, N):
#     if n == 1:
#         if N % 2 == 0:
#             l.append('1 2')
#         else:
#             l.append('1 3')
#         return
#     # recursive call for n-1
#     hanoi(n - 1, l, N)
#     peg = int(l[-1][2])
#
#
# ## n%2 == 0: 1->2
#
#
# if __name__ == '__main__':
#     N = int(input())
#     trace = []
#     hanoi(N, trace, N)
#     print(len(trace))
#     for s in trace:
#         print(s)

# codes reference: https://pacific-ocean.tistory.com/119

n = int(input())
def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)
