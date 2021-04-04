import sys

input = sys.stdin.readline

N = int(input())
mod = 1000000
p = int(mod / 10 * 15)  # 피사노주기에 의해 M = 10^k 일 때, k > 2 라면, 주기는 항상 15 × 10^(k-1) 입니다
fibo = [0] * p
fibo[1] = 1

for i in range(2, p):
    fibo[i] = fibo[i - 1] + fibo[i - 2]
    fibo[i] %= mod

print(fibo[N % p])
