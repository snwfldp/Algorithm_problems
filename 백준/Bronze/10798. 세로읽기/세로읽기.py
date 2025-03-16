a = [input().strip() for i in range(5)]
res = ""

for j in range(15):
    for k in a:
        if j < len(k):
            res += k[j]

print(res)