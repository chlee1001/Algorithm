import sys

input = sys.stdin.readline

razer = list(input().rstrip())
# print(razer)

answer = 0
stack = []

for i in range(len(razer)):
    if razer[i] == '(':
        stack.append('(')
    else:
        if razer[i - 1] == '(':  # )가 왔는데 이전이 바로 (일 경우
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)
