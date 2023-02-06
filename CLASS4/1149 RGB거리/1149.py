import sys
input = sys.stdin.readline

n = int(input())
llist =[[] for _ in range(n+1)]

for i in range(1,n+1):
    a, b, c = map(int, input().split())
    llist[i] = [a, b, c]

result = [[0, 0, 0] for _ in range(n+1)]

result[1] = [llist[1][0], llist[1][1], llist[1][2]]

for i in range(2, n+1):
    for j in range(3):
        a = (j+1)%3
        b = (j+2)%3
        result[i][j] = min(result[i-1][a], result[i-1][b])+llist[i][j]

print(min(result[n]))
