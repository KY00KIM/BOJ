import sys

n, e = map(int, input().split())
inf = int(1e9)
graph = [[inf]*(n+1)for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split() )
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

result = 0
if graph[1][v1]==inf or graph[v1][v2]== inf or graph[v2][n]==inf:
    print(-1)
else:
    result = graph[1][v1]+graph[v1][v2]+graph[v2][n]
    print(result)