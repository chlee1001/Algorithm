import sys

input = sys.stdin.readline

T = int(input())


def lowLevelSort(trees):
    new_trees = [0] * len(trees)
    for i in range(len(trees)):
        if (i + 1) % 2 == 1:
            new_trees[i // 2] = trees[i]
        else:
            new_trees[len(trees) - (i // 2 + 1)] = trees[i]
    return new_trees


for _ in range(T):
    N = int(input())
    log_trees = list(map(int, input().split()))
    log_trees = lowLevelSort(sorted(log_trees))

    max_level = 0
    for i in range(N - 1):
        if abs(log_trees[i] - log_trees[i + 1]) > max_level:
            max_level = abs(log_trees[i] - log_trees[i + 1])

    if abs(log_trees[-1] - log_trees[0]) > max_level:
        max_level = abs(log_trees[-1] - log_trees[0])

    print(max_level)
