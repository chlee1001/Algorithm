def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print("재귀적으로: ", gcd(192, 162))

import math

print("라이브러리 이용:", math.gcd(192, 162))
