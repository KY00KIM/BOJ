import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [(0,0)]
for _ in range(n):
    weg, val = map(int, input().split())
    data.append((weg, val))

arr = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= data[i][0]:
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-data[i][0]]+data[i][1])
        else:
            arr[i][j] = arr[i-1][j]

        
        
print(arr[n][k])