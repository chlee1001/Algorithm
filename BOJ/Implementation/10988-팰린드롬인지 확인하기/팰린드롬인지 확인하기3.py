import sys

input = sys.stdin.readline

input_string = list(input().rstrip())
compare_string = list(reversed(input_string))

if input_string == compare_string:
    print(1)
else:
    print(0)
