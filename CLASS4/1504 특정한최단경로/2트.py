import sys
import heapq

n, e = map(int, input().split())
inf = int(1e9)
graph = [[]for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split() )
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())
result = []

order = [(1, v1), (v1, v2), (v2, n)]

for i in range(3):
    start = order[i][0]
    end = order[i][1]
    distance = [inf]*(n+1)
    distance[start]= 0
    now = start
    heap = []
    heapq.heappush(heap,(0,start))
    
    for i in graph[start]:
        distance[i[1]] = i[0]    

    while heap:
        dist, now = heapq.heappop(heap)
        
        if distance[now] <dist :
            continue
    
        for edge in graph[now]:
            cost = dist + edge[0]
            if cost<distance[edge[1]]:
                distance[edge[1]] = cost
                heapq.heappush(heap, (cost, edge[1]))
    
    if distance[end] == inf:
        result.append(-1)
    else: 
        result.append(distance[end])
    
        

    
if result.count(-1):
    print(-1)
else: 
    sum = 0
    for i in range(3):
        sum += result[i]
    print(sum)