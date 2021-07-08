import sys

input = sys.stdin.readline
N = int(input())
cnt = 0

for _ in range(N):
    stack = []
    word = list(input().rstrip())

    while word:
        temp = word.pop()
        if not stack:
            stack.append(temp)
        else:
            if stack[-1] == temp:
                stack.pop()
            else:
                stack.append(temp)
    if not stack:
        cnt += 1

print(cnt)
