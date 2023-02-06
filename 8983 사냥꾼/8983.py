import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
hunter  = list(map(int, input().split()))
hunter.sort()
animal = []
for _ in range(n): 
    x, y = map(int, input().split())
    animal.append((x,y))

res =0

for i in animal:
    x = i[0]
    far = l-i[1]
    if far < 0 : continue
    start = 0
    end = m-1
    while start<=end:
        mid = (start+end)//2
        xh = hunter[mid]
        if x-far<= xh and xh<=(x+far):
            res+=1
            break
        elif xh < x-far:
            start = mid+1
        else: end = mid-1
    
print(res)