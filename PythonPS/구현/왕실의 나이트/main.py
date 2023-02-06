
data = input()
x = int(data[1])
y = ord(data[0])-ord("a")+1

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
result = 0

for i in range(8):
    flag = True
    nx = x+dx[i]
    ny = y+dy[i]
    if nx < 1 or nx>8 or ny<1 or ny>8:
        flag = False
    if flag:
        result+=1

print(result)