A, B = input().split()

for i in range(2, -1, -1):
    if A[i] > B[i]:
        print(A[::-1])
        break
    elif A[i] < B[i]:
        print(B[::-1])
        break
