parent = [0, 1, 2, 3, 4, 5]

def find(parent, a):
    if a != parent[a]:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b]=a
    else:
        parent[a]= b
        
union(parent, 0, 3)

print(f"union 0, 3 : {parent}")

union (parent, 1, 2)

print(f"union 1, 2 : {parent}")

union (parent, 1, 3)

print(f"union 1, 3 : {parent}")


union (parent, 4, 5)

print(f"union 4, 5 : {parent}")

print(f"result : ", end = "")
for i in range(6):
    print(find(parent, i), end=" ")
print()
