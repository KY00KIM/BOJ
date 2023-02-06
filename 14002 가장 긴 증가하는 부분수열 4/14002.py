import sys
input = sys.stdin.readline

n = int(input())
data = [0]+ list(map(int, input().split()))

dp = [[] for _ in range(n+1)]
info = [(0,0)] #cnt, endNum

def getIdx(info, target):
    res = 0
    llen  = 0
    for i in range(len(info)):
        if info[i][1] < target and info[i][0] >= llen:
            res = i
            llen = info[i][0]
    return res

def getMaxIdx(info):
    res = 0
    tmp = 0
    for i in range(1, len(info)):
        if info[i][0] > tmp: res = i
    return res

for i in range(1, n+1):
    strIdx = getIdx(info, data[i])
    dp[i] = dp[strIdx] + [data[i]]
    info.append((info[strIdx][0]+1,data[i]))

res = getMaxIdx(info)
print(info[res][0])
for i in range(info[res][0]):
    print(dp[res][i], end=" ")    
    