n = int(input())
count = 0

# 큰 단위부터 화폐 확인
coin_types = [500, 100, 50, 10, 5, 1]
change = 1000 - n

for coin in coin_types:
    count += change // coin
    change %= coin

print(count)
