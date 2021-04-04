import sys

input = sys.stdin.readline
fibo = [-1] * 10001
fibo[0] = 0
fibo[1] = 1

N = int(input())

for i in range(2, N + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

print(fibo[N])