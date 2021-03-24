import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priority_list = list(map(int, input().split()))
    docs_list = list(range(len(priority_list)))
    docs_list[M] = 'target'

    order = 0

    while True:
        num = priority_list[0]
        if num == max(priority_list):
            order += 1

            if docs_list[0] == 'target':
                print(order)
                break
            else:
                priority_list.pop(0)
                docs_list.pop(0)
        else:
            priority_list.append(priority_list.pop(0))
            docs_list.append(docs_list.pop(0))
