import sys

input = sys.stdin.readline

N, P = map(int, input().split())

melody = [[] for _ in range(7)]
count = 0
for _ in range(N):
    a, b = map(int, input().split())
    if melody[a]:
        if melody[a][-1] < b:
            melody[a].append(b)
            count += 1
        elif melody[a][-1] > b:
            while melody[a][-1] > b:
                melody[a].pop()
                count += 1
                if not melody[a]:
                    break
            if melody[a] and melody[a][-1] == b:
                continue
            else:
                melody[a].append(b)
                count += 1

        elif melody[a][-1] == b:
            continue

    else:
        melody[a].append(b)
        count += 1

print(count)
