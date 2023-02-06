import sys
input = sys.stdin.readline
n = int(input())
data = [0] + list(map(int, input().split()))
result = [0]*(n+1)

for i in range(1, n+1):
	for j in range(i):
		if data[j] < data[i]:
			result[i] = max(result[i], result[j]+1)

print(max(result))

