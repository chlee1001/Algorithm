import sys
from collections import deque

T = int(input())

for _ in range(T):
    comm = input()
    N = int(sys.stdin.readline())

    temp = input()[1:-1]
    if ',' not in temp and temp != "":
        num_list = deque([int(temp)])
    elif temp != "":
        num_list = deque(map(int, temp.split(',')))
    else:
        num_list = deque()

    flag = True
    cnt = 0  # Reverse의 개수

    for i in range(len(comm)):
        if comm[i] == "R":
            cnt += 1
        else:
            if len(num_list) == 0:
                flag = 0
                break

            if cnt % 2 == 0:
                num_list.popleft()
            else:
                num_list.pop()

    if cnt % 2 == 1:
        num_list.reverse()

    if flag:
        print("[", end="")
        for i in range(len(num_list)):
            if i == len(num_list) - 1:
                print(num_list[i], end="")
            else:
                print(str(num_list[i]) + ",", end="")
        print("]")
    else:
        print('error')
