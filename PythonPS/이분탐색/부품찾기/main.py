import sys
n = int(sys.stdin.readline().rstrip())
llist = list(map(int, input().split()))
llist.sort()
m = int(input())
request = list(map(int, input().split()))
result = []

for item in request:
    start, end = 0, n-1
    flag = False
    while start <= end:
        mid = (start+end)//2
        if llist[mid]==item:
            flag = True
            break
        elif item > llist[mid]:
            start = mid +1
        else:
            end = mid - 1
    if flag:
        result.append("yes")
    else:
        result.append("no")


for i in result:
    print(i, end=" ")