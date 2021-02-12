import sys
import math

N = int(sys.stdin.readline())
n = math.ceil((math.sqrt(9+12*(N-1))+3)/6)
print(n)

# For testing
"""
while True:
    N = int(sys.stdin.readline())
    if N == -1:
        break
    n = math.ceil((math.sqrt(9+12*(N-1))+3)/6)
    print(f'{N}: {n}')
"""