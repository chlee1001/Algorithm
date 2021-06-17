N = input()
exp = 0
result = 0
while exp < len(N) - 1:
    result += 9 * (10 ** exp) * (exp + 1)
    exp += 1
result += (int(N) - (10 ** (len(N) - 1)) + 1) * len(N)
print(result)

"""
시간 초과
N = int(input())
new_num = ""
for i in range(1, N + 1):
    new_num += str(i)

print(len(new_num))
"""
