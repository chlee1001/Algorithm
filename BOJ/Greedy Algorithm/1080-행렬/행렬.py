import sys

input = sys.stdin.readline
n, m = map(int, input().split())

matrix_a = []
matrix_b = []

for i in range(n):
    matrix_a.append(list(input().strip()))

for i in range(n):
    matrix_b.append(list(input().strip()))

matrix_a = sum(matrix_a, [])
matrix_b = sum(matrix_b, [])
# print(matrix_a)
# print(matrix_b)

index = 0
result, count = 0, 0
if n*m %3==0:
    while True:
        if index >= n * m:
            break
        if index % n == 0:
            if count > result:
                result = count
            count=0
        if matrix_a[index] != matrix_b[index]:
            count += 1
        # print(matrix_a[index], matrix_b[index])
        index += 1
else:
    print(-1)
print(result)
