from collections import deque
from xml.etree.ElementPath import find

def findNext(visited, N, M, start):
    for i in range(start,N*M):
        if visited[i//M][i%M]==0:
            return i
    return -1

def BFS(visited, N, M):
    result = 0
    queue = deque()
    start = 0
        
    start=findNext(visited, N, M, start)
    
    while start != -1:
        queue.append(start)

        while queue:
            node = queue.popleft()
            x = node // M
            y = node % M
            visited[x][y] = 1
            
            if x > 0:
                if not visited[x-1][y]: queue.append((x-1)*M + y)
            if y > 0:
                if not visited[x][y-1]: queue.append(x*M + y-1)
            if x < N-1:
                if not visited[x+1][y]: queue.append( (x+1)*M + y)
            if y < M-1:
                if not visited[x][y+1]: queue.append(x*M + y + 1 )
                
        result += 1
        start = findNext(visited, N, M, start)
            

    
    return result




N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for i in range(N):
    line = input()
    for j in range(M):
        graph[i].append(int(line[j]))

print(BFS(graph, N, M))