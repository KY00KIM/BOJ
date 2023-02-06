import sys
input = sys.stdin.readline

n = 10
llist = [[],
         [2, 3],
         [1, 4, 5],
         [1, 6, 7],
         [2], [2],
         [3], [3]]
visited = [False] * 8

queue = [1]
while queue:
    now = queue.pop(0)
    print(f"{now} >> ", end="")
    visited[now] = True
    for i in llist[now]:
        if not visited[i]:
            queue.append(i)

print()
print(visited)
        

