import sys

input = sys.stdin.readline

N, M = map(int, input().split())
cards_list = list(map(int, input().split()))

max_sum = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if M >= cards_list[i] + cards_list[j] + cards_list[k] > max_sum:
                max_sum = cards_list[i] + cards_list[j] + cards_list[k]

print(max_sum)
