n = int(input())
a = []
for _ in range(n):
    start, end = map(int, input().split())
    a.append((end, start))

a.sort()

b = 0
c = 0

for end, start in a:
    if start >= c:
        b += 1
        c = end

print(b)