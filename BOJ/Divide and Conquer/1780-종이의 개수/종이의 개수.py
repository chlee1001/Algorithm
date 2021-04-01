import sys

input = sys.stdin.readline

N = int(input())
paper_list = [list(map(int, input().split())) for _ in range(N)]
result = []


def check_same(x, y, d):
    paper = paper_list[x][y]
    for i in range(x, x + d):
        for j in range(y, y + d):
            if paper_list[i][j] != paper:
                return False
    return True


def solution(x, y, d):
    if check_same(x, y, d):
        if paper_list[x][y] == 1:
            result.append(1)
        elif paper_list[x][y] == 0:
            result.append(0)
        elif paper_list[x][y] == -1:
            result.append(-1)
    else:
        d //= 3
        solution(x, y, d)
        solution(x + d, y, d)
        solution(x + 2 * d, y, d)

        solution(x, y + d, d)
        solution(x + d, y + d, d)
        solution(x + 2 * d, y + d, d)

        solution(x, y + 2 * d, d)
        solution(x + d, y + 2 * d, d)
        solution(x + 2 * d, y + 2 * d, d)


solution(0, 0, N)
print(result.count(-1))
print(result.count(0))
print(result.count(1))
