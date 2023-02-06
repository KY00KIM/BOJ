from collections import deque

N, M = map(int, input().split())
graph = []
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, input())))


def bfs(x, y):   
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        if (x, y) == (N-1, M-1):
            break
    
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if nx <0 or nx > N-1 or ny < 0 or ny > M-1 or graph[nx][ny]==0 :
                continue
            elif nx==0 and ny == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny]= graph[x][y]+1
                queue.append((nx, ny))
    return graph[N-1][M-1]

print(bfs(0,0))        
        

    