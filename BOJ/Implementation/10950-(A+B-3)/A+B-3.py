import sys

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    print(n + m)
