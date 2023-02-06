import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
inf = int(1e9)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

res = [0]*(n)

for node in range(1, n+1):
    dist = [inf]*(n+1)
    visited=[False]*(n+1)
    dist[node] = 0
    Q = []
    heapq.heappush(Q, [0, node])
    while Q:
        cost, now = heapq.heappop(Q)
        if visited[now]: continue
        visited[now] = True
        for edge in graph[now]:
            dist[edge[1]] = min(dist[edge[1]], edge[0] + dist[now])
            heapq.heappush(Q, [dist[edge[1]], edge[1]])
    
    if node == x:
        for i in range(n):
            res[i] += dist[i+1]
    else:
        res[node-1] += dist[x]

print(max(res))            
