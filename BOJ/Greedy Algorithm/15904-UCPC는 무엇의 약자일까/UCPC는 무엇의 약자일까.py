import sys

input = sys.stdin.readline

string = input().rstrip()

check_alpha = ['U', 'C', 'P', 'C']

flag = True
for alpha in check_alpha:
    if alpha in string:
        string = string[string.index(alpha) + 1:]
    else:
        flag = False
        break

print("I love UCPC") if flag else print("I hate UCPC")
