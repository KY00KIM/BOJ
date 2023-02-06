import sys
input = sys.stdin.readline

n = int(input())
data = [0]+list(map(int, input().split()))
dp = [[] for _ in range(n+1)]

'''
a1 => res < a1
len > O(1)
an => an 포함할 수 있는 AND 가장 긴 수열
'''

for i in range (1,n+1):
    target = 0
    for j in range(1,i):
        if dp[j] and data[i] > dp[j][-1] and len(dp[j])>len(dp[target]):
            target = j
    dp[i] = dp[target]+[data[i]]

res = 0
for i in range(1, n+1):
    if len(dp[i])>len(dp[res]):
        res = i
print(len(dp[res]))
for i in range(len(dp[res])):
    print(f"{dp[res][i]} ", end="")
    