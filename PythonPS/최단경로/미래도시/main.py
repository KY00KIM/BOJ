import sys

inf = int(1e9)

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[inf]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if not i or not j:
            graph[i][j] = inf
        elif i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
x, k = map(int, input().split())

for via in range(1, n+1):
    for start in range(1, n+1):
        for end in range (1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][via]+graph[via][end])
    
if graph[1][k] == inf or graph[k][x] == inf:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])
