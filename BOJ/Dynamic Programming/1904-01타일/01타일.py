import sys

input = sys.stdin.readline

n = int(input())
result_list = [0] * 1000001
result_list[1] = 1
result_list[2] = 2

for i in range(3, n + 1):
    result_list[i] = (result_list[i - 1] + result_list[i - 2]) % 15746

print(result_list[n])
