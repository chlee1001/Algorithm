import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    string = list(input().rstrip())
    while len(string) != 0:
        if string[0] == ')':
            print("NO")
            break
        else:
            if ')' in string:
                string.remove(')')
                string.remove('(')
            else:
                print("NO")
                break

    if len(string) == 0:
        print("YES")
