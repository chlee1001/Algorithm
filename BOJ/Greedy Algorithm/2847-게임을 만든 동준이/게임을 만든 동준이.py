import sys

input = sys.stdin.readline

N = int(input())
levels = [int(input()) for _ in range(N)]

result = 0
max_level = levels[-1]
for i in range(N - 2, -1, -1):
    if levels[i] >= max_level:
        temp = max_level - 1
        result += levels[i] - temp
        max_level = levels[i] = temp
    else:
        max_level = levels[i]

print(result)
