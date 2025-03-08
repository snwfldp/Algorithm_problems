a = int(input())
for _ in range(a):
    data = list(map(int, input().split()))
    n = data[0]
    scores = data[1:]
    avg = sum(scores) / n
    above_avg = len([score for score in scores if score > avg])
    percentage = (above_avg / n) * 100
    print(f"{percentage:.3f}%")