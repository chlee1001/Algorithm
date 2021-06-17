import sys

input = sys.stdin.readline

A, B = map(int, input().split())

cur_value = 1
position = 1
result = 0

for i in range(A, B + 1):
    while position < i:
        cur_value += 1
        position += cur_value
    result += cur_value

print(result)
