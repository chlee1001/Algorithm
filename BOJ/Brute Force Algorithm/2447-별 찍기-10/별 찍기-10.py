import sys

input = sys.stdin.readline

N = int(input())
arr = [['*'] * N for _ in range(N)]  # output array 생성

temp = N
cnt = 0
while temp != 1:  # 입력받은 n이 3의 몇승?
    temp /= 3
    cnt += 1


'''
1, 4, 7, 10, 13, 16, 19, 22, 25 .... 3으로 나눈 나머지가 1인 부분이 공백
전체를 봤을때, 3줄씩 한 세트라고 하면, 3, 4, 5, 12, 13, 14, 21, 22, 23....  (n//3)%3==1인 부분이 공백
'''
for i in range(cnt):
    idx = []
    for j in range(N):
        if (j // 3 ** i) % 3 == 1:
            idx.append(j)
    for row in idx:
        for col in idx:
            arr[row][col] = ' '

print('\n'.join([''.join([str(i) for i in row]) for row in arr]))
