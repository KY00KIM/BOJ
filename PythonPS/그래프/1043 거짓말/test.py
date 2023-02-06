n, m = 9, 4
data = list(map(int, input().split()))
k = data[0]
known = data[1:k+1]
parent = [i for i in range(n+1)]
llist = [[]for _ in range(m)]
root = 0
        

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b        
        
for i in range(k-1):
    union_parent(parent, known[i], known[i+1])
    root = find_parent(parent, known[i])


print(f"root is {root}")
print(parent)