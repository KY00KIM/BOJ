import sys
input = sys.stdin.readline


# N movement, p1 right, p2 left, p3 up, p4 down
#{p1, p2}  {p3, p4}
n, a, b, c, d = map(int, input().split())
a = a / 100
b = b / 100
c = c / 100
d = d / 100
p = [a, b, c, d]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = []

def solution(visit, cnt, curPos, curPb):
    if not cnt: return curPb
    global n
    visit.append((curPos[0],curPos[1]))
    res = 0
    for i in range(4):
        nx = curPos[0]+dx[i]
        ny = curPos[1]+dy[i]
        flag = True
        if (nx, ny) in visit:
           continue
        res += solution(visit, cnt-1, (nx, ny), curPb*p[i])
    visit.pop()
    return res
        
ans = solution(visited,  n, (0,0), 1)

print(ans)