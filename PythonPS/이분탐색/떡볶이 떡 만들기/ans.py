n, m = map(int, input().split())

llist = list(map(int, input().split()))
llist.sort()
result = [0]

start = 0
end = llist[n-1]
find = (start+end)//2

while start<=end:
    sum = 0
    for i in llist:
        if i > find:
            sum += i-find
    
    if sum >= m:
        result.append(find)
        start = find+1
    else:
        end = find-1
    
    find = (start+end)//2

print(result[-1])