import sys

input = sys.stdin.readline

N = int(input())

count = 0
input_car = {}
output_car = []

for i in range(N):
    input_car[input().rstrip()] = i

for i in range(N):
    output_car.append(input().rstrip())

for i in range(N - 1):
    for j in range(i + 1, N):
        if input_car[output_car[i]] > input_car[output_car[j]]:
            count += 1
            break

print(count)
