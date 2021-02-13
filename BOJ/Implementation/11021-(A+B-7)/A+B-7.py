import sys

input = sys.stdin.readline

test_case = int(input())

for i in range(test_case):
    n, m = map(int, input().split())
    print(f"Case #{i + 1}: {n + m}")
