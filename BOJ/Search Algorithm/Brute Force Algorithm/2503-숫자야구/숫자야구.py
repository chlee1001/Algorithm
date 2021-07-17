import sys
from itertools import permutations

input = sys.stdin.readline

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cases = list(permutations(num, 3))

N = int(input())
for _ in range(N):
    ques, s_c, b_c = map(int, input().split())
    ques = list(str(ques))

    temp_cases = []
    for i in range(len(cases)):
        strike, ball = 0, 0
        for j in range(3):
            if cases[i][j] == int(ques[j]):
                strike += 1
            elif int(ques[j]) in cases[i]:
                ball += 1
        if s_c == strike and b_c == ball:
            temp_cases.append(cases[i])

    # 한 줄 끝나고, 맞은 케이스만 사용할 수 있도록
    cases = temp_cases

print(len(cases))
