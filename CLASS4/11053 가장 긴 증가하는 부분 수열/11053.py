import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

result = [[[0,0]]*n for _ in range(n)]

for i in range(n):
    result[i][i] = (1, data[i])

for i in range(1, n):
    for j in range(n-i):
        if data[j+i] > result[j][j+i-1][1] and data[j+i] > result[j-1][j+i][1]:
            result[j][j+i] = [max(result[j][j+i-1][0], result[j-1][j+i][0]) + 1, data[j+i]]
        elif data[j+i] > result[j][j+i-1][1]:
            if result[j][j+i-1][0]+1 > result[j-1][j+i][0]:
                result[j][j+i] = [result[j][j+i-1][0]+ 1, data[j+i]]
            else: result[j][j+i] = [result[j-1][j+i][0], result[j-1][j+i][1]]
        elif data[j+i] > result[j-1][j+i][1]:
            if result[j-1][j+i][0]+1 > result[j][j+i-1][0]:
                result[j][j+i] = [result[j-1][j+i][0]+ 1, data[j+i]]
            else: result[j][j+i] = [result[j][j+i-1][0], result[j][j+i-1][1]]
        else:
            if result[j-1][j-i][0] > result[j][j-i-1][0]:
                result[j][j+i] = [result[j-1][j+i][0], result[j-1][j+i][1]]
            else: 
                result[j][j+i] = [result[j][j+i-1][0], result[j][j+i-1][1]]

print(result[0][n-1][0])

