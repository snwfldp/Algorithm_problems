import sys

a = sys.stdin.read().split()
x = [int(a[0]), int(a[2]), int(a[4])]
y = [int(a[1]), int(a[3]), int(a[5])]

for i in x:
    if x.count(i) == 1:
        _x = i
        break

for j in y:
    if y.count(j) == 1:
        _y = j
        break

print(_x, _y)