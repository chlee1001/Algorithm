import sys

input = sys.stdin.readline

while True:
    try:
        n, m = map(int, input().split())
        print(n + m)
    except:
        break
