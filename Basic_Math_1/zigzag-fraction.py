import sys
import math

X = int(sys.stdin.readline())
n = math.ceil((math.sqrt(1+8*X)-1)/2)
x = int(n*(n+1)/2-X)
if n % 2 == 0:
    print(f'{n-x}/{1+x}')
else:
    print(f'{1+x}/{n-x}')

# For testing
"""
while True:
    X = int(sys.stdin.readline())
    if X == -1:
        break
    n = math.ceil((math.sqrt(1+8*X)-1)/2)
    x = int(n*(n+1)/2-X)
    if n % 2 == 0:
        print(f'{X}: {n-x}/{1+x}')
    else:
        print(f'{X}: {1+x}/{n-x}')
"""
