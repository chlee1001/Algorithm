import sys

input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

result = 0
for i in range(n):
    result += A[i] * B[i]

print(result)
