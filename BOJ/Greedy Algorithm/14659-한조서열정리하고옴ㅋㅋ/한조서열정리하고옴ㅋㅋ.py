import sys

input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))
maxHeight = 0
score = 0
result = 0

for height in heights:
    if height > maxHeight:
        maxHeight = height
        score = 0
    else:
        score += 1
    result = max(result, score)

print(result)
