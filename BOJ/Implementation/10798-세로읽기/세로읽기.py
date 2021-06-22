import sys

input = sys.stdin.readline

input_string = [list(input().rstrip()) for _ in range(5)]

for i in range(15):
    for j in range(5):
        if not input_string[j]:
            continue
        else:
            print(input_string[j].pop(0), end="")
