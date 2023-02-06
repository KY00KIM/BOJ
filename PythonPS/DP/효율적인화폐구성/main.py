import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

arr = [0]+[-1]*(m)

for total in range(1, m+1):
    tmp = 10001
    for j in range(n):
        if total<data[j]:
            continue
        if arr[total-data[j]] != -1:
            tmp = min(tmp, arr[total-data[j]]+1)
    if tmp == 10001:
        continue
    else:
        arr[total]=tmp
        
print(arr[m])
        