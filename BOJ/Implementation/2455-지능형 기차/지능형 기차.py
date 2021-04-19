import sys

input = sys.stdin.readline

max_p = 0
sum_p = 0
for _ in range(4):
    out_p, in_p = map(int, input().split())
    sum_p -= out_p
    sum_p += in_p
    max_p = max(max_p, sum_p)

print(max_p)
