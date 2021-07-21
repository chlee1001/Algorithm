import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    price_list = sorted(map(int, input().split()), reverse=True)
    dc_list = []

    while price_list:
        price = price_list.pop()

        if price * 100 // 75 in price_list:
            dc_list.append(price)
            price_list.remove(price * 100 // 75)

    print("Case #{0}: ".format(t + 1), end="")
    print(*dc_list)
