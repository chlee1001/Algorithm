import sys

input = sys.stdin.readline

T = int(input())
words = [list((input().rstrip())) for _ in range(T)]

# print(words)

count = 0

for i in range(T):
    group_check = []
    for ch in words[i]:
        if group_check:
            if ch == group_check[-1]:
                group_check.append(ch)
                continue
        if ch in group_check:
            break
        else:
            group_check.append(ch)
    if len(group_check) == len(words[i]):
        count += 1

print(count)
