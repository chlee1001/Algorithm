import sys

input = sys.stdin.readline

init_string = list(input().rstrip())
N = int(input())
string2 = []

for _ in range(N):
    comm = list(input().split())
    if comm[0] == 'P':
        init_string.append(comm[1])
    elif comm[0] == 'L':
        if init_string:
            string2.append(init_string.pop())
    elif comm[0] == 'D':
        if string2:
            init_string.append(string2.pop())
    elif comm[0] == 'B':
        if init_string:
            init_string.pop()

print(''.join(init_string + list(reversed(string2))))
