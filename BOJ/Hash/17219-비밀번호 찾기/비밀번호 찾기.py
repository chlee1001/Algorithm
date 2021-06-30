import sys

input = sys.stdin.readline

N, M = map(int, input().split())

password = {}

for _ in range(N):
    url, pwd = input().split()
    password[url] = pwd

for _ in range(M):
    url = input().rstrip()
    print(password[url])
