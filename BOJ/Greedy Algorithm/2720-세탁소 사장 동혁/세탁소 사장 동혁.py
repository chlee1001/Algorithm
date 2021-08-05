import sys

input = sys.stdin.readline
T = int(input())

# quarter = 25
# Dime = 10
# Nickel = 5
# Penny = 1
for _ in range(T):
    quarter, dime, nickel, penny = 0, 0, 0, 0  # 각 동전 개수
    C = int(input())
    while C > 0:
        if C >= 25:  # Quarter
            quarter += C // 25
            C %= 25
        elif C >= 10:  # Dime
            dime += C // 10
            C %= 10
        elif C >= 5:  # Nickel
            nickel += C // 5
            C %= 5
        elif C >= 1:  # Penny
            penny += C // 1
            C -= penny

    print(quarter, dime, nickel, penny)
