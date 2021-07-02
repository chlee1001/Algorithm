import sys

input = sys.stdin.readline

N, M = map(int, input().split())

Team = {}
for _ in range(N):
    team_name = input().rstrip()
    Team[team_name] = []
    members = int(input())
    for _ in range(members):
        Team[team_name].append(input().rstrip())

for _ in range(M):
    name = input().rstrip()
    flag = int(input())
    if flag:  # 팀 이름만 출력
        for team, member in Team.items():
            if name in member:
                print(team)
    else:  # 멤버 전체 사전순 출력
        print('\n'.join(sorted(Team[name])))
