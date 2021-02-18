import sys

input = sys.stdin.readline

n = int(input())

positive_list = []
negative_list = []
result = 0
for _ in range(n):
    temp = int(input())
    if temp > 1:
        positive_list.append(temp)
    elif temp == 1:
        result += 1
    elif temp <= 0:
        negative_list.append(temp)

positive_list.sort(reverse=True)
negative_list.sort()

for i in range(0, len(positive_list), 2):
    if i + 1 < len(positive_list):  # 양수 리스트의 개수가 홀수여서 맨 마지막 한개가 남는 경우를 걸러내기 위해
        result += positive_list[i] * positive_list[i + 1]
    else:
        result += positive_list[i]

for i in range(0, len(negative_list), 2):
    if i + 1 < len(negative_list):  # 음수 리스트의 개수가 홀수여서 맨 마지막 한개가 남는 경우를 걸러내기 위해
        result += negative_list[i] * negative_list[i + 1]
    else:
        result += negative_list[i]

print(result)