import sys

input = sys.stdin.readline

N, P = map(int, input().split())

W, L, G = map(int, input().split())

hacking = {}
for _ in range(P):
    name, WL = input().rstrip().split()
    hacking[name] = WL

score = 0
for _ in range(N):
    name = input().rstrip()
    if name in hacking.keys():
        if hacking[name] == 'W':
            score += W
        else:
            score -= L
    else:
        score -= L

    if score < 0:
        score = 0
    elif score >= G:
        print('I AM NOT IRONMAN!!')
        exit(0)

print('I AM IRONMAN!!')
