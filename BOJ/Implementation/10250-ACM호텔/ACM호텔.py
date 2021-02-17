test_case = int(input())
for _ in range(test_case):
    h, w, n = map(int, input().split())
    y = n % h
    x = n // h + 1
    if y == 0:
        y = h
        x -= 1

    print(y * 100 + x)
