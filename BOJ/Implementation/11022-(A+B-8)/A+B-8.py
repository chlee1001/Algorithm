import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    print(f"Case #{i + 1}: {n} + {m} = {n + m}")
