M = int(input())
N = int(input())

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

prime = [a for a in range(M, N + 1) if is_prime(a)]

if prime:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)
