import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
answer = 0
sugang = []

for _ in range(N):
    P, L = map(int, input().split())
    mileages = list(map(int, input().split()))
    heapq.heapify(mileages)

    available = L - P
    if available > 0:
        heapq.heappush(sugang, 1)
    else:
        for i in range(abs(available)):
            heapq.heappop(mileages)
        heapq.heappush(sugang, heapq.heappop(mileages))

count = 0
while sugang:
    sugang_mileage = heapq.heappop(sugang)
    if M - sugang_mileage >= 0:
        M -= sugang_mileage
        count += 1
    else:
        break
print(count)
