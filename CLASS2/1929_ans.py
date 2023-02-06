m, n = (input().split())
m = int(m)
n = int(n)

nums = [False, False] + [True]*(n-1)
prime = []

for i in range (2, n+1):
    if nums[i]:
        prime.append(i)
        for j in range(i*2, n+1, i):
            nums[j] = False
        
for i in prime:
    if i >= m and i<= n:
        print(i)

    

