import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]


def check_BW(slice_board):
    # print(slice_board)
    black_cnt = 0  # black 시작 [bwbwbwbw],[wbwbwbwb]
    for row in range(8):
        for col in range(8):
            if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1): # 0,2,4,8 칸
                if slice_board[row][col] != "B":
                    black_cnt += 1
            if (row % 2 == 0 and col % 2 == 1) or (row % 2 == 1 and col % 2 == 0): # 1,3,5,7 칸
                if slice_board[row][col] != "W":
                    black_cnt += 1

    white_cnt = 0  # white 시작 [wbwbwbwb],[bwbwbwbw]
    for row in range(8):
        for col in range(8):
            if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
                if slice_board[row][col] != "W":
                    white_cnt += 1
            if (row % 2 == 0 and col % 2 == 1) or (row % 2 == 1 and col % 2 == 0):
                if slice_board[row][col] != "B":
                    white_cnt += 1

    return min(black_cnt, white_cnt)


check = []
for row in range(N - 7):
    for col in range(M - 7):
        cnt1, cnt2 = 0, 0
        # 체스판 경우의 수 slicing
        c = [board[row + i][col:col + 8] for i in range(8)]
        # c = [c[(0 + col):(8 + col)] for c in board[(0 + row):(8 + row)]]
        check.append(check_BW(c))
print(min(check))
