n = int(input())
times = list(map(int, input().split()))
times.sort()  # 오름차순 정렬

waiting_time = 0  # 각 사람이 기다리는 시간
total_time = 0  # 모든 사람들이 수행한 시간
for i in times:
    waiting_time += i
    total_time += waiting_time

print(total_time)
