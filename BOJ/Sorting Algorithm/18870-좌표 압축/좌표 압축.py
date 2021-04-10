import sys

input = sys.stdin.readline

N = int(input())

coord_list = list(map(int, input().split()))
new_list = sorted(list(set(coord_list)))

d = {}
for i in range(len(new_list)):
    d[new_list[i]] = i

for i in coord_list:
    print(d[i], end=" ")
