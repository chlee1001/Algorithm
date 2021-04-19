import sys

input = sys.stdin.readline

# 0: 배
# 1: 등

# 도(0,111), 개(00,11), 걸(000,1), 윷(0000), 모(1111)

for _ in range(3):
    lists = list(map(int, input().split()))

    front = 0  # 배
    rear = 0  # 등

    for num in lists:
        if num == 0:
            front += 1
        else:
            rear += 1

    if rear == 0 and front == 4:
        print('D')
    elif rear == 1 and front == 3:
        print('C')
    elif rear == 2 and front == 2:
        print('B')
    elif rear == 3 and front == 1:
        print('A')
    elif rear == 4 and front == 0:
        print('E')
