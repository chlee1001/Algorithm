import sys

input = sys.stdin.readline

for _ in range(3):
    lists = list(map(int, input().split()))

    if lists.count(1) == 0:
        print('D')
    elif lists.count(1) == 1:
        print('C')
    elif lists.count(1) == 2:
        print('B')
    elif lists.count(1) == 3:
        print('A')
    elif lists.count(1) == 4:
        print('E')
