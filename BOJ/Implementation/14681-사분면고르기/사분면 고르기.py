x = int(input())
y = int(input())

if 0 < x <= 1000 and 0 < y <= 1000:
    print(1)
elif -1000 <= x < 0 and 0 < y <= 1000:
    print(2)
elif 0 > x >= -1000 and 0 > y >= -1000:
    print(3)
elif 0 < x <= 1000 and -1000 <= y < 0:
    print(4)
