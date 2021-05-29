import sys

input = sys.stdin.readline

N = int(input())
file_list = [list(input().rstrip()) for _ in range(N)]

input_word = file_list[-1]

for i in range(N - 1):
    for j in range(len(input_word)):
        if input_word[j] == file_list[i][j]:
            continue
        else:
            input_word[j] = '?'

print(''.join(input_word))
