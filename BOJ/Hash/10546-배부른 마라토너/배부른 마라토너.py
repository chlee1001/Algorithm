import sys

input = sys.stdin.readline

N = int(input())

participants = {}
for _ in range(N):
    participant = input().rstrip()
    if participant in participants:
        participants[participant] += 1
    else:
        participants[participant] = 0

for _ in range(N - 1):
    participants[input().rstrip()] += 1

for key, value in participants.items():
    if value % 2 == 0:
        print(key)
        break
    else:
        continue
