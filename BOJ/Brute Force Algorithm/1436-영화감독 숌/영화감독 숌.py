import sys

input = sys.stdin.readline

N = int(input())

title = 666
cnt = 0
while True:
    if '666' in str(title):
        cnt += 1
        if cnt == N:
            print(title)
            break
    title += 1
