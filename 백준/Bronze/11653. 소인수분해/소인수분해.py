import sys
import math

N = int(sys.stdin.readline())
if N == 1:
    sys.exit()

i = 2
while i * i <= N:
    while N % i == 0:
        print(i)
        N //= i
    i += 1

if N > 1:
    print(N)