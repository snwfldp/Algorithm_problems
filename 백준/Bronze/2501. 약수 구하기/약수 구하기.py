N, K = map(int, input().split())
a = 0
for i in range(1, N + 1):
    if N % i == 0:
        a += 1
        if a == K:
            print(i)
            break
else:
    print(0)