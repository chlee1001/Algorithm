import sys

input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

budgets.sort()

start = 0
end = max(budgets)
total_budget = 0
result = 0

if sum(budgets) <= m:
    print(max(budgets))
else:
    while start <= end:
        mid = (start + end) // 2

        total_budget = 0
        for budget in budgets:
            if budget >= mid:
                total_budget += mid
            else:
                total_budget += budget

        if total_budget > m:
            end = mid - 1
        else:
            start = mid + 1
            result = mid
    print(result)
