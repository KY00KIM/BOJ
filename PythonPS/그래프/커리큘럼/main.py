import sys
input = sys.stdin.readline

n = int(input())
lectures = [[] for i in range(n+1)]
lecDegree = [0]*(n+1)
lecTime = [0]
lecLv = [-1]*(n+1)
lecSeq = []
result = []

def totalIime(lecLv, lecTime,target):
    lv = lecLv[target]
    total = lecTime[target]
    for curLv in range(lv):
        largestLv = 0
        for j in range(1, n+1):
            if lecLv[j] == curLv:
                if largestLv < lecTime[j]:
                    largestLv = lecTime[j]
        total += largestLv
    return total


for i in range(1,n+1):
    llist = list(map(int, input().split()))
    for j in range(len(llist)-1):
        if j == 0:
            lecTime.append(llist[j])
        else:
            lectures[j].append(i)
            lecDegree[i]+=1

queue = []
for i in range(1, n+1):
    if lecDegree[i] == 0:
        queue.append(i)
        lecLv[i] = 0
        
while queue:
    now = queue.pop(0)
    
    for target in lectures[now]:
        lecDegree[target] -= 1
        if lecDegree[target] == 0:
            queue.append(target)
            lecLv[target] = lecLv[now]+1
    
    lecSeq.append(now)
    
for i in range(1, n+1):
    print(totalIime(lecLv, lecTime, i))
