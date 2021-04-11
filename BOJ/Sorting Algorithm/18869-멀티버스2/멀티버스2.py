import sys

input = sys.stdin.readline

M, N = map(int, input().split())

space_list = [list(map(int, input().split())) for _ in range(M)]

new_space_list = [[] for _ in range(M)]
dictionary = {}
for i in range(M):
    new_list = sorted(list(set(space_list[i])))
    for j in range(len(new_list)):
        dictionary[new_list[j]] = j
    for x in (space_list[i]):
        new_space_list[i].append(dictionary[x])

new_space_list.sort()
cnt, ans = 1, 0
for i in range(1, M):
    if new_space_list[i] == new_space_list[i - 1]:
        cnt += 1
    else:
        ans += cnt * (cnt - 1) // 2
        cnt = 1

ans += cnt * (cnt - 1) // 2
print(ans)
