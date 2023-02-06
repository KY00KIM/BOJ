import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

arr.sort(reverse=True)

for i in range(1,m+1):
    if i%(k+1) == 0:
        ans+= arr[1]
    else:
        ans += arr[0]
        
print(ans)