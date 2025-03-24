n = int(input())
if n == 1:
    print(1)
else:
    a = 1
    b = 0
    while a < n:
        b += 1
        a += 6 * b
    print(b + 1)
