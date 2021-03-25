import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
pick_list = list(map(int, input().split()))
count = 0

num_list = deque([x for x in range(1, N + 1)])

for i in range(M):
    num_len = len(num_list)
    num_index = num_list.index(pick_list[i])

    if num_index < num_len - num_index:  # 왼쪽에 가까우면
        while True:
            if num_list[0] == pick_list[i]:
                num_list.popleft()
                break
            else:
                num_list.rotate(-1)
                count += 1
    else:  # 오른쪽에 가까우면
        while True:
            if num_list[0] == pick_list[i]:
                num_list.popleft()
                break
            else:
                num_list.rotate(1)
                count += 1

print(count)
