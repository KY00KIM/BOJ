import copy

n, m = map(int, input().split())
a, b, dir = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
mmap = []
for _ in range(n):
    mmap.append(list(map(int, input().split())))
    
result = 1    
visited = copy.deepcopy(mmap)
visited[a][b] = 1

def chkContinue(x, y):
    flag = False
    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if not visited[nx][ny]:
            flag = True
    return flag

while True:
    if not chkContinue(a, b):
            if mmap[a-dx[dir]][b-dx[dir]]:
                break
            a -=dx[dir]
            b -=dy[dir]
            continue
    
    dir = (dir+3)%4
    
    if visited[a+dx[dir]][b+dy[dir]]:
        continue
    else:
        a = a+dx[dir]
        b = b+dy[dir]
        visited[a][b] = 1
        result+=1
        print(a, b)
        
    
print(result)