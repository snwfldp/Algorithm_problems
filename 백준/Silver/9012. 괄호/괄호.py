n = int(input())
for i in range(n):
    a = input().strip()
    cnt = 0
    b = True
    for j in a:
        if j == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                b = False
                break
    if cnt != 0:
        b = False
    print("YES" if b else "NO")
