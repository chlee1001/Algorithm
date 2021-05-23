import sys

input = sys.stdin.readline

papers = [[0 for _ in range(101)] for _ in range(101)]

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            papers[j][i] = 1

result = 0
for row in papers:
    result += row.count(1)

print(result)
