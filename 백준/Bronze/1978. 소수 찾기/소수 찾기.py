def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
num = list(map(int, input().split()))
res = 0
for j in num:
    if is_prime(j):
        res += 1
print(res)
