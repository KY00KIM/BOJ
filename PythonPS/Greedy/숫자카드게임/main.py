import sys
input = sys.stdin.readline

n, m = map(int, input().split())
llist = []
ans = 0

for i in range(n):
    llist.append(list(map(int, input().split())))
    llist[i].sort()

for i in range(n):
    if llist[i][0] > ans: ans = llist[i][0]
    
print(ans)