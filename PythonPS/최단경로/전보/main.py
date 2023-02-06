import sys
import heapq

input = sys.stdin.readline
inf = int(1e9)

n, m, c = map(int, input().split())

graph= [[]for _ in range(n+1)]
distance = [inf]*(n+1)
heap = []

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    

distance[c] = 0
heapq.heappush(heap, (0,c))

while heap:
    dist, cur = heapq.heappop(heap)
    
    if dist > distance[cur]:
        continue
    
    for edge in graph[cur]:
        target = edge[0]
        cost = edge[1] + dist
    
        if cost < distance[target]:
            distance[target] = cost
            heapq.heappush(heap, (cost, target))

cnt = 0
largest = 0

for i in range(1, n+1):
    if i == c or distance[i] == inf:
        continue
    cnt += 1
    if largest < distance[i]: 
        largest = distance[i] 

print(f"{cnt} {largest}")
    