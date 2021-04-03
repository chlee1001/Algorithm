import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A_matrix = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B_matrix = [list(map(int, input().split())) for _ in range(M)]

result_matrix = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            result_matrix[n][k] += A_matrix[n][m] * B_matrix[m][k]

for row in result_matrix:
    for value in row:
        print(value, end=" ")
    print()
