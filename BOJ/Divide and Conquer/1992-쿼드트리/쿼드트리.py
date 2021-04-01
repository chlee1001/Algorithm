import sys

input = sys.stdin.readline

N = int(input())

pixel_list = [list(map(int, input().rstrip())) for _ in range(N)]

result = []


def check_same(x, y, d):
    pixel = pixel_list[x][y]
    for i in range(x, x + d):
        for j in range(y, y + d):
            if pixel_list[i][j] != pixel:
                return False
    return True


def solution(x, y, d):
    if check_same(x, y, d):
        if pixel_list[x][y]:
            result.append(1)
        else:
            result.append(0)
    else:
        d //= 2
        result.append('(')
        solution(x, y, d)
        solution(x, y + d, d)
        solution(x + d, y, d)
        solution(x + d, y + d, d)
        result.append(')')


solution(0, 0, N)
for x in result:
    print(x, end="")
