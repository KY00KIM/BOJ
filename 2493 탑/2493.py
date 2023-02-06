import sys
input = sys.stdin.readline

n = int(input())
tower = [0]+list(map(int, input().split()))
res = [0]*(n+1)

'''
from the end of index to the start > push
next index in respect to stack top is
1. bigger or same  = pop and write it on res and push it
2. if smaller => push it
'''
stack = []
for i in range(n, 0, -1):
    if not stack:
        stack.append((tower[i], i))
    else:
        while stack:
            if tower[i] >= stack[-1][0]:
                now = stack.pop()
                res[now[1]] = i
            else:
                stack.append((tower[i], i)) 
                break
        if not stack:
            stack.append((tower[i], i))
while stack:
    now = stack.pop()
    res[now[1]] = 0

for i in range(1, n+1):
    print(f"{res[i]} ", end="")
            