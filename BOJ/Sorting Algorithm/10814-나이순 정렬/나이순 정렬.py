import sys

input = sys.stdin.readline

n = int(input())

member_list = []

for _ in range(n):
    member_list.append(list(input().split()))

member_list.sort(key=lambda members: int(members[0]))

for member in member_list:
    print(member[0], member[1])
