import sys

input=sys.stdin.readline # 시간제한을 위해서

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    grades = []
    count = 0
    for _ in range(n):
        resume, interview = map(int, input().split())
        grades.append((resume, interview))

    grades.sort(key=lambda x: (x[0]))  # resume 등수 순대로... 오름차순 정렬

    count += 1
    interview_min = grades[0][1]
    for i in range(1, n):
        if grades[i][1] < interview_min:
            count += 1
            interview_min = grades[i][1]

    print(count)
