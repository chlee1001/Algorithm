n = int(input())
meetings = []
for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key=lambda x: (x[1], x[0]))  # 튜플을 이용해서 두번째 원소(끝나는 시간)로 오름차순 정렬 후, 첫번째 원소(시작하는 시간)로 오름차순 정렬

count = end_time = 0

# meeting 리스트를 하나씩 확인
for meeting in meetings:
    s, e = meeting
    if s >= end_time:  # 시작시간이 끝나는 시간보다 크거나 같으면 회의개수 하나 증가, 끝나는 시간 갱신
        count += 1
        end_time = e

print(count)
