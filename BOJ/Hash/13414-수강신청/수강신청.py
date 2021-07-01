import sys

input = sys.stdin.readline

K, L = map(int, input().split())

queue_list = {}

for i in range(L):
    studentId = input().rstrip()
    queue_list[studentId] = i

for id in sorted(queue_list.items(), key=lambda x: x[1])[:K]:
    print(id[0])
