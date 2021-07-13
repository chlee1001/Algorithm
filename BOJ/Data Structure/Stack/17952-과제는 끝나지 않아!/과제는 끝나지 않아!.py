import sys

input = sys.stdin.readline

N = int(input())
# 1 A T: 과제O, 점수, 걸린 시간

work_list = []
score = 0
for _ in range(N):
    info = list(map(int, input().split()))
    if info[0] == 1:  # 과제를 받았으면
        if info[2] - 1 > 0:
            work_list.append((info[1], info[2] - 1))
        else:
            score += info[1]
    else:  # 과제가 없으면
        if work_list:
            work = work_list.pop()
            if work[1] - 1 > 0:
                work_list.append((work[0], work[1] - 1))
            else:
                score += work[0]

print(score)
