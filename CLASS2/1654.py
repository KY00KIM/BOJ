def findLength(list, N):
    length=0
    find = 0
    
    llist = []
    
    for cable in list:
        length+=cable
    
    length /= N
    find = length

    while find:
        cnt = 0
        find /= 2
        for cable in list:
            cnt += cable // length
        if cnt >= N :
            llist.append(int(length))
            length += find
        else : 
            length -= find
        
    return max(llist)
        

K, N = input().split()
K = int(K)
N = int(N)
li = []
for i in range(K): 
    li.append(int(input())) 

print(findLength(li, N))