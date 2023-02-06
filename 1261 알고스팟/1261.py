import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph=[[] for _ in range(m)]
inf = int(1e9)
dist = [[inf] * n for _ in range(m)]
visited = [[False]*n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(m):
    graph[i] = list(map(int,input().rstrip()))

dist[0][0] = 0
Q = []
heapq.heappush(Q, [0, 0, 0])

while Q:
    cost, x, y = heapq.heappop(Q)
    if visited[x][y]: continue
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<= nx <m and 0<=ny<n:
            dist[nx][ny] = min(dist[nx][ny], dist[x][y]+graph[nx][ny])   
            heapq.heappush(Q, [dist[nx][ny], nx, ny])

print(dist[m-1][n-1])   