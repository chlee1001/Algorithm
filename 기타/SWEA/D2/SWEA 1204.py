import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    test_case = int(input())
    score_list = list(map(int, input().split()))
    score_list.sort(reverse=True)
    students = {}
    for i in range(101):
        students[i] = 0
    for score in score_list:
        students[score] += 1
    max_value = max(students.values())
    result=0
    for key, value in students.items():
        if value == max_value:
            result = key
    print("#{0} {1}".format(test_case, result))
    # print(max(students.values()))
