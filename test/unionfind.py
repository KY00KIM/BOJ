parent = [i for i in range(5)]

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find( parent, b)
    if a>b:
        parent[a] = b
    else: parent[b] = a


for _ in range(3):
    b, c = map(int, input().split())
    union(parent, b, c)
        
print(parent)