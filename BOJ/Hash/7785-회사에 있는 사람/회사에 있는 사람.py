import sys

input = sys.stdin.readline

N = int(input())

exist = {}

for i in range(N):
    name, action = (input().split())
    exist[name] = action

exist = sorted(exist.items(), reverse=True)

for i in range(len(exist)):
    if exist[i][1] == 'leave':
        continue
    else:
        print(exist[i][0])


