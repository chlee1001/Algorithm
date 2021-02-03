import math

# M과 N을 입력받기
m, n = map(int, input().split())
array = [True for i in range(n + 1)]  # 처음에는 모든 수가 소수(True)인 것으로 초기화
array[1] = 0  # 1은 소수가 아님

# 에라토느테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True:  # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 제거하기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# M부터 N까지의 모든 소수 출력
for i in range(m, n + 1):
    if array[i]:
        print(i)
