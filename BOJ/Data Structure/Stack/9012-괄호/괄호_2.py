import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    string = list(input().rstrip())

    vps_sum = 0
    for x in string:
        if x == '(':
            vps_sum += 1
        elif x == ')':
            vps_sum -= 1
        if vps_sum < 0:
            print("NO")
            break

    if vps_sum == 0:
        print('YES')
    elif vps_sum > 0:
        print('NO')
