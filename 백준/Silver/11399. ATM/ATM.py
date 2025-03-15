n = int(input())
time = list(map(int, input().split()))

time.sort()

a = 0
total = 0
for i in time:
    a += i
    total += a

print(total)
