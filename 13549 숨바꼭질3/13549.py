import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
inf = int(1e9)
Q = []
#dist = [n-i for i in range(n)] + [i-n for i in range(n,100001)]
dist = [inf]*100001
dist[n] = 0

heapq.heappush(Q, [0, n])
while Q:
    cost, now = heapq.heappop(Q)
    if dist[now] < cost: continue
    
    if now>0 and cost+1 < dist[now-1]:
        dist[now-1] = cost+1
        heapq.heappush(Q, [cost+1, now-1])
    if now<100000 and cost+1 < dist[now+1]:
        dist[now+1] = cost+1
        heapq.heappush(Q, [cost+1, now+1])
    if now*2 <= 100000 and cost < dist[now*2]:
        dist[now*2] = cost
        heapq.heappush(Q, [cost, now*2])
    
print(dist[k])    
        