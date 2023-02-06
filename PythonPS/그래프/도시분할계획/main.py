import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
edges = [ ]
result = []
parent = [i for i in range (n+1)]
ans = 0

for _ in range(m):
    a, b, c = map( int, input().split())
    edges.append((a, b, c))


edges = sorted(edges, key = lambda x:x[2])

for edge in edges:
    if find_parent(parent, edge[0]) == find_parent(parent, edge[1]):
        continue
    union_parent(parent, edge[0], edge[1])
    result.append(edge)
    
for i in range(len(result)-1):
    ans+= result[i][2]
    
print(ans)