import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 4가지 모두 이용하려면, M>6
count = 0
if N == 1:
    count = 1
elif N == 2:  # 세로가 2이면, 2번/3번 방법만 사용가능 --> 오른쪽으로 두칸씩
    count = min(4, (M + 1) // 2)
elif M < 7:  # N>=3, M<7 --> 오른쪽으로 한칸씩
    count = min(4, M)
else:  # N>=3, M>7 --> 2,3번 한번 나머지 1,4번
    count = M - 2

print(count)
