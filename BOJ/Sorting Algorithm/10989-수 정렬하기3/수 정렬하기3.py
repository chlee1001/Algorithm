import sys

input = sys.stdin.readline

n = int(input())
cnt_list = [0] * 10001
for i in range(n):
    cnt_list[int(input())] += 1

for i in range(10001):
    if cnt_list[i] != 0:
        for j in range(cnt_list[i]):
            print(i)
