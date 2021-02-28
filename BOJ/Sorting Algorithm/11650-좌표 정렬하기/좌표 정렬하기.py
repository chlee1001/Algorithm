import sys

input = sys.stdin.readline

n = int(input())

coord_list = []

for _ in range(n):
    coord_list.append(list(map(int, input().split())))

coord_list.sort(key=lambda coord: (coord[0], coord[1]))

for coord in coord_list:
    print(coord[0], coord[1])
