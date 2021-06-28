import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pocket_dict = {}
pocket_dict2 = {}

for i in range(N):
    pocketmon_name = input().rstrip()
    pocket_dict[i + 1] = pocketmon_name
    pocket_dict2[pocketmon_name] = i + 1

for i in range(M):
    quiz = input().rstrip()
    if quiz.isdigit():  # 숫자일 경우
        print(pocket_dict[int(quiz)])
    else:  # 영어일 경우
        print(pocket_dict2[quiz])
