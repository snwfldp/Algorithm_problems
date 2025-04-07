a = int(input())
b = int(input())
c = int(input())
d = a * b * c
d = str(d)
cnt = [0] * 10

for i in d:
    cnt[int(i)] += 1
for j in cnt:
    print(j)