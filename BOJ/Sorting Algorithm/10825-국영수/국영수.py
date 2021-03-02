import sys

input = sys.stdin.readline

n = int(input())
students = []
for _ in range(n):
    students.append(list(input().split()))

"""
1. 국어 점수 내림차순
2. 영어 점수 오름차순
3. 수학 점수 내림차순
4. 영어 이름 오름차순
"""
students.sort(key=lambda student: (-int(student[1]), int(student[2]), -int(student[3]), student[0]))

for student in students:
    print(student[0])
