import sys
from collections import deque
input = sys.stdin.readline

# N >> K 
# 
# -1, +1, *2
def enqueue(queue, visited, data):
    visited[data] = True
    if data-1 <= 100000 and data-1 >= 0 and not visited[data-1]:
        queue.append(data-1)
    if data+1 <= 100000 and data+1 >= 0 and not visited[data+1]:
        queue.append(data+1)
    if data*2 <= 100000 and data*2 >= 0 and not visited[data*2]:
        queue.append(data*2)
    return


def updateVal (dist, data):
    if data-1 <= 100000 and data-1 >= 0 :
        dist[data-1] = min(dist[data-1], dist[data]+1)
    if data+1 <= 100000 and data+1 >= 0 :
        dist[data+1] = min(dist[data+1], dist[data]+1)
    if data*2 <= 100000 and data*2 >= 0 :
        dist[data*2] = min(dist[data*2], dist[data]+1)


def solution(n, k):
    dist = [n-i for i in range(n)] + [i-n for i in range(n, 100001)]
    visited = [False]*100001
    queue = deque()
    
    queue.append(n)
    enqueue(queue, visited, n)
    while queue:
        now = queue.popleft()
        updateVal(dist, now)
        enqueue(queue, visited, now)

    return dist[k]    
                    
    

n, k = map(int, input().split())
print(solution(n, k))
