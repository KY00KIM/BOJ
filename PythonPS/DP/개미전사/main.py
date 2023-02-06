import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

arr = [0]*n
arr[0] = data[0]
arr[1] = max(data[1], data[0])

for i in range(2, n):
    arr[i] = max(data[i]+arr[i-2], arr[i-1])
    
print(arr[n-1])