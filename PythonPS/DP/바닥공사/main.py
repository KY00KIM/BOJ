import sys
input = sys.stdin.readline

n = int(input())

arr = [0, 1, 3] + [0]*(n-2)

for i in range(3, n+1):
    arr[i] = arr[i-1] + arr[i-2]*2

print(arr[n]%796796)