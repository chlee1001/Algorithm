n, k = map(int, input().split())

coin_types = []
for _ in range(n):
    coin_types.append(int(input()))

coin_types.sort(reverse=True)  # 내림차순 정렬

count = 0
for coin in coin_types:
    if k == 0: break # k가 0이 되었으면 종료 >> 시간 단축
    count += k // coin
    k %= coin

print(count)
