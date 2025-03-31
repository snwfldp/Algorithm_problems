import sys
output = []
for line in sys.stdin:
    n = int(line.strip())
    if n == -1:
        break
    a = [i for i in range(1, n // 2 + 1) if n % i == 0]
    if sum(a) == n:
        output.append(f"{n} = " + " + ".join(map(str, a)))
    else:
        output.append(f"{n} is NOT perfect.")
print("\n".join(output))