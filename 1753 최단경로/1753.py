import heapq

v, e = map(int, input().split())
k = int(input())
inf = int(1e9)
graph = [[] for _ in range(v+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

visited = [False]*(v+1)
dist = [inf]*(v+1)
dist[k] = 0
Q = []
heapq.heappush(Q, [0,k])
while Q:
    data = heapq.heappop(Q)
    cost, now = data[0], data[1]
    if visited[now] : continue
    visited[now] = True
    for edge in graph[now]:
        dist[edge[0]] = min(dist[edge[0]], dist[now]+edge[1])
        heapq.heappush(Q, [dist[edge[0]],edge[0]])

for i in range(1, v+1):
    if dist[i] == inf:
        print("INF")
    else: 
        print(dist[i])
        
    