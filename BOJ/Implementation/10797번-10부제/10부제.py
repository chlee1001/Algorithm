N = int(input())
car_list = list(map(int, input().split()))

count = 0

for car in car_list:
    if N == car:
        count += 1

print(count)
