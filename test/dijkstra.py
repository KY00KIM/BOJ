import sys
from xmlrpc.client import NOT_WELLFORMED_ERROR
input = sys.stdin.readline

n = 5
llist = [[] for _ in range(9)]
inf = int(1e9)

for i in range(6):
    a, b, c = map(int, input().split())
    llist[a].append((b, c))

visited = [False]*(n+1)
distance = [inf]*(n+1)
distance[1]= 0
for i in llist[1]:
    distance[i[0]] = i[1]

for i in range(n-1):
    now = 0
    dist = inf
    for j in range(1,n+1):
        if not visited[j] and dist > distance[j]:
            dist = distance[j]
            now = j
    visited[now] = True
    for target in llist[now]:
        cost = distance[now]+target[1]
        distance[target[0]] = min(distance[target[0]], cost)

print(distance)