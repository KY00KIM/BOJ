m, n = (input().split())
m = int(m)
n = int(n)

nums = [i for i in range(2, n+1)]
prime = []

while nums:
    token = nums.pop(0)
    prime.append(token)
    
    for j in nums:
        if j % token == 0 :
            nums.remove(j)
    
        
for i in prime:
    if i >= m and i<= n:
        print(i)

    

