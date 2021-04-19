import sys

input = sys.stdin.readline

lists = list(map(int, input().split()))

result = 0
for num in lists:
    result += num ** 2

print(result % 10)
