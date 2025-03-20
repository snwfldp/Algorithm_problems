N, B = map(int, input().split())

arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ""

while N > 0:
    res = arr[N % B] + res
    N //= B

print(res)
