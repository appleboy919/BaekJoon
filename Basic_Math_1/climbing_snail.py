import sys
import math

A, B, V = map(int, sys.stdin.readline().split())
n = math.ceil((V-A)/(A-B)+1)
print(n)

# For testing
"""
while True:
    A, B, V = map(int, sys.stdin.readline().split())
    if A == -1:
        break
    n = math.ceil((V-A)/(A-B)+1)
    print(f'{A} {B} {V}: {n}')
"""
