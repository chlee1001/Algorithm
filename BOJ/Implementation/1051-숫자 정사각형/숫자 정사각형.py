import sys

input = sys.stdin.readline

N, M = map(int, input().split())
rectangle = [list(map(int, input().rstrip())) for _ in range(N)]

max_edge = min(N, M)
result = 0
for i in range(N):
    for j in range(M):
        for k in range(max_edge):
            if i + k < N and j + k < M:
                if rectangle[i][j] == rectangle[i][j + k] == rectangle[i + k][j] == rectangle[i + k][j + k]:
                    result = max(result, (k + 1) ** 2)
print(result)
