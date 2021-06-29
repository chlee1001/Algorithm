import sys

input = sys.stdin.readline

N = int(input())

sell_items = {}

for _ in range(N):
    book_name = input().rstrip()
    if book_name in sell_items:
        sell_items[book_name] += 1
    else:
        sell_items[book_name] = 1

max_sell = max(sell_items.values())

best_seller = []
for book, count in sell_items.items():
    if count == max_sell:
        best_seller.append(book)

print(sorted(best_seller)[0])
