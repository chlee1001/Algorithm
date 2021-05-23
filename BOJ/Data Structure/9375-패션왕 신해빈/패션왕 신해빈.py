import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    clothes = {}
    N = int(input())
    for _ in range(N):
        name, kind = input().split()
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1

    case = 1
    for key in clothes.keys():
        case = case * (clothes[key] + 1)
    print(case - 1)
