import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    result = [(a ** i) % 10 for i in range(1, 5)]
    result = result[(b % 4) - 1]
    if result != 0:
        print(result)
    else:
        print(10)
