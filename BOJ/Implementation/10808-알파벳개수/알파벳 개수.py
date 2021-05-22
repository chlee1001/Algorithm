import sys

input = sys.stdin.readline

string = list(input().rstrip())

alpha_count = {}
for i in range(ord('z') - ord('a') + 1):
    alpha_count[chr(ord('a') + i)] = 0

for alphabet in string:
    alpha_count[alphabet] += 1

print(*list(alpha_count.values()))
