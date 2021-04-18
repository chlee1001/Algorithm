import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

test_case = int(input())


def dfs(v):
    global result
    team[v] = True
    cycle.append(v)
    num = arr[v]

    if not team[num]:
        dfs(num)
    else:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return


for _ in range(test_case):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    team = [True] + [False] * N
    result = []

    for i in range(1, N + 1):
        if not team[i]:
            cycle = []
            dfs(i)
    print(N - len(result))
