import sys

input = sys.stdin.readline

N, K = map(int, input().split())
mod = 1000000007


def power(a, b):
    if b == 0:
        return 1
    else:
        if b % 2 == 0:  # B가 짝수일 때
            return (power(a, b // 2) ** 2) % mod
        else:
            return (power(a, b // 2) ** 2 * a) % mod


# Factorial dp
fact = [1 for _ in range(N + 1)]

for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % mod

child = fact[N]
parent = (fact[K] * fact[N - K]) % mod

# 페르마의 소정리
print((child % mod) * (power(parent, mod - 2) % mod) % mod)

# -------------------------------------------------
# for i in range(2, N + 1):
#     fact[i] = fact[i - 1] * i
#
# child = fact[N]
# parent = fact[K] * fact[N - K]

# print(int(child / parent) % mod) ==> 메모리초과
