import sys

input = sys.stdin.readline

input_string = [[0] * 15 for _ in range(5)]

for i in range(5):
    temp = list(input().rstrip())
    for j in range(len(temp)):
        input_string[i][j] = temp[j]

for i in range(15):
    for j in range(5):
        if input_string[j][i] == 0:
            continue
        else:
            print(input_string[j][i], end="")
