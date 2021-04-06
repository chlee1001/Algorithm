import sys

input = sys.stdin.readline

while True:
    edge_list = list(map(int, input().split()))
    edge_list.sort()
    if edge_list[0] == 0:
        break
    if edge_list[0] ** 2 + edge_list[1] ** 2 == edge_list[2] ** 2:
        print('right')
    else:
        print("wrong")
