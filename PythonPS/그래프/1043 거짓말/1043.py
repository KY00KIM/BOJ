import sys
input = sys.stdin.readline

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
        

n, m = map(int, input().split())
data = list(map(int, input().split()))
k = data[0]
known = data[1:k+1]
parent = [i for i in range(n+1)]
llist = [[]for _ in range(m)]
root = 0
result = 0
        
for i in range(k-1):
    union_parent(parent, known[i], known[i+1])


for i in range(m):
    data = list(map(int, input().split()))
    llist[i]=data
    for j in range(1,len(data)-1):
        union_parent(parent, data[j], data[j+1])

for i in range(1, n+1):
    find_parent(parent, i)

if known:
    root = find_parent(parent, known[0])
    

for i in range(m):
    flag = True
    num = llist[i][0]
    for j in range(1, num+1):
        if parent[llist[i][j]]==root:
            flag = False
            break
    if flag:
        result += 1

print(result)