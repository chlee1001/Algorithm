import sys

input = sys.stdin.readline

N = int(input())

paper_list = [list(map(int, input().split())) for _ in range(N)]

result = []  # white(0), blue(1)


def check_same(x, y, d):
    color = paper_list[x][y]
    for i in range(x, x + d):
        for j in range(y, y + d):
            if paper_list[i][j] != color:
                return False
    return True


def solution(x, y, d):
    if check_same(x, y, d):
        if paper_list[x][y]:
            result.append(1)
        else:
            result.append(0)
    else:
        d //= 2
        solution(x, y, d)
        solution(x + d, y, d)
        solution(x, y + d, d)
        solution(x + d, y + d, d)


solution(0, 0, N)
print(result.count(0))
print(result.count(1))
