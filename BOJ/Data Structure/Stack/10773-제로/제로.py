import sys

input = sys.stdin.readline

K = int(input())

stack_list = []
for _ in range(K):
    comm = int(input())
    if comm == 0:
        stack_list.pop()
    else:
        stack_list.append(comm)

print(sum(stack_list))