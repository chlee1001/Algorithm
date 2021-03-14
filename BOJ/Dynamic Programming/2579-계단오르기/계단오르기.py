import sys

input = sys.stdin.readline

n = int(input())

steps_list = []
dp = []
for _ in range(n):
    steps_list.append(int(input()))
if n == 1:
    print(steps_list[0])

elif n == 2:
    print(max(steps_list[0] + steps_list[1], steps_list[1]))
elif n == 3:
    print(max(steps_list[0] + steps_list[2], steps_list[1] + steps_list[2]))
else:
    dp.append(steps_list[0])
    dp.append(max(steps_list[0] + steps_list[1], steps_list[1]))
    dp.append(max(steps_list[0] + steps_list[2], steps_list[1] + steps_list[2]))

    for i in range(3, n):
        dp.append(max(dp[i - 2] + steps_list[i], dp[i - 3] + steps_list[i - 1] + steps_list[i]))

    print(dp.pop())
