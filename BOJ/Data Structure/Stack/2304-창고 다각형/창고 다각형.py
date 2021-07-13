import sys

input = sys.stdin.readline

N = int(input())
pillars = []
for _ in range(N):
    idx, height = map(int, input().split())
    pillars.append((idx, height))

pillars.sort(key=lambda x: x[0])  # 정렬

max_pillar = max(pillars, key=lambda x: x[1])  # 가장 높은 기둥찾기

# 땅에 기둥세우기
area = [0] * (pillars[-1][0] + 1)
for idx, height in pillars:
    area[idx] = height
max_index = area.index(max_pillar[1])  # 높은 기둥의 인덱스찾기

temp = 0
total = 0
# 왼쪽부터 가장 높은 기둥까지
for i in range(max_index + 1):
    if area[i] > temp:
        temp = area[i]
    total += temp

temp = 0
# 오른쪽부터 가장높은 기둥까지
for i in range(pillars[-1][0], max_index, -1):
    if area[i] > temp:
        temp = area[i]
    total += temp

print(total)
