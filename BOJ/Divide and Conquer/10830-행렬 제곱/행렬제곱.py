import sys

input = sys.stdin.readline

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


def matrix_multiple(a, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                a[i][j] %= 1000
        return a
    else:
        if b % 2 == 0:  # 제곱수가 짝수일 때 AAAAAA --> (A^2)^2^2
            temp_matrix = [[0 for _ in range(N)] for _ in range(N)]
            c = matrix_multiple(a, b // 2)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        temp_matrix[i][j] += c[i][k] * c[k][j]
                    temp_matrix[i][j] %= 1000
            return temp_matrix

        else:  # AAAAA --> (A^2)^2 * A
            temp_matrix = [[0 for _ in range(N)] for _ in range(N)]
            c = matrix_multiple(a, b - 1)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        temp_matrix[i][j] += c[i][k] * a[k][j]
                    temp_matrix[i][j] %= 1000
            return temp_matrix


result = matrix_multiple(matrix, B)
for row in result:
    for value in row:
        print(value, end=" ")
    print()
