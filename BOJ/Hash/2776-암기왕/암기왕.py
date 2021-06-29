import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    N_Note = set(map(int, input().split()))

    M = int(input())
    M_Note = list(map(int, input().split()))

    for num in M_Note:
        if num in N_Note:
            print(1)
        else:
            print(0)
