n = int(input())
N = n
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            continue
        elif word[j] in word[j+1:]:
            N -= 1
            break
print(N)