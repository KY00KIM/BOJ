import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_parent(parent, x):
    if x != parent[x]:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(parent, a, b)
    elif op == 1:
        x = find_parent(parent, a)
        y = find_parent(parent, b)
        print(f"{a} and {b} : ", end = " ")
        if x == y:
            print("YES")
        else:
            print("NO")
        print(parent)
            
