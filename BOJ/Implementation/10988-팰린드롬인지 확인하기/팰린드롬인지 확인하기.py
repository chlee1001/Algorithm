import sys

input = sys.stdin.readline

input_string = list(input().rstrip())

while len(input_string) >= 1:
    if len(input_string) == 1:
        break
    elif input_string[0] == input_string[-1]:
        input_string.pop(0)
        input_string.pop(-1)
    else:
        print(0)
        exit(0)

print(1)
