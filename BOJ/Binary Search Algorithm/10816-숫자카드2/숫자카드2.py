import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

hashmap = {}
for a in A:
    if a in hashmap:
        hashmap[a] += 1
    else:
        hashmap[a] = 1

for b in B:
    if b in hashmap:
        print(hashmap[b], end=" ")
    else:
        print(0, end=" ")

# print(' '.join(str(hashmap[b]) if b in hashmap else '0' for b in B))
