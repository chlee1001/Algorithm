import sys

input = sys.stdin.readline

N = list(input().rstrip())
N.sort(reverse=True)

each_sum = 0

if '0' not in N:
    print(-1)
else:
    for x in N:
        each_sum += int(x)

    if each_sum % 3 == 0:
        print(''.join(N))
    else:
        print(-1)

'''
30배수 조건:
각 자리수 합이 3의 배수
1의 자리 0
'''
