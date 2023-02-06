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

stack = [1]

while stack:
    now = stack.pop()
    print(f"{now} >> ", end="")
    visited[now] = True
    
    for edge in llist[now]:
        if not visited[edge]:
            stack.append(edge)

print()
print(visited)

        

