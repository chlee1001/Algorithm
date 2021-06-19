import sys

input = sys.stdin.readline


def check(arr):
    n = len(board)
    answer = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):  # 열 순회하면서 연속 숫자 세기
            if arr[i][j] == arr[i][j - 1]:  # 이전것과 같으면 cnt+1
                cnt += 1
            else:  # 이전 것과 다르면  cnt=1 초기화
                cnt = 1
            if cnt > answer:
                answer = cnt

        cnt = 1
        for j in range(1, n):  # 행 순회하면서 연속 숫자 세기
            if arr[j][i] == arr[j - 1][i]:  # 이전것과 같으면 cnt+1
                cnt += 1
            else:  # 이전 것과 다르면  cnt=1 초기화
                cnt = 1
            if cnt > answer:
                answer = cnt

    return answer


N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(N):
        if j + 1 < N:  # 열 체크
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # 인접 교환
            temp = check(board)
            if temp > result:
                result = temp
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # 원복

        if i + 1 < N:  # 행 체크
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]  # 인접 교환
            temp = check(board)
            if temp > result:
                result = temp
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]  # 원복

print(result)
