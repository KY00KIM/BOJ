import sys


import sys, heapq
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [[] for _ in range(m)]
for _ in range(m):
    graph[_] = list(map(int, input().split()))
start = list(map(int, input().split()))
end = list ( map(int, input().split()))
inf = int(1e9)
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]
start[0] -= 1
start[1] -= 1
end[0] -= 1
end[1] -= 1
'''
    4
2       1
    3
'''

dist = [[inf]*n for _ in range(m)]
dist[start[0]][start[1]] = 0
dirtable = [[-1]*n for i in range(m)]
Q = []
heapq.heappush(Q, [0,start[0], start[1], start[2]])
while Q:
    cost, x, y, curdir = heapq.heappop(Q)
    if dist[x][y] < cost : continue
    dirtable[x][y] = curdir
    for dir in range(1,5):
        for scale in range(1, 4):
            nx = x + dx[dir] * scale
            ny = y + dy[dir] * scale
            if  nx<0 or ny < 0 or nx > m-1 or ny > n-1 or graph[nx][ny]: break
        
            newCost = 1
            if curdir == dir: newCost += 0
            elif (dir+curdir)%4 == 3: 
                newCost += 2
            else : 
                newCost += 1
            if dist[nx][ny] > (newCost + dist[x][y]):
                dist[nx][ny] = newCost + dist[x][y]
                heapq.heappush(Q, [dist[nx][ny], nx, ny, dir])

res = dist[end[0]][end[1]]
curdir = dirtable[end[0]][end[1]]
if curdir == end[2]: res+= 0
elif (curdir+end[2])%4 ==3 : res += 2
else : res += 1

print(res)
