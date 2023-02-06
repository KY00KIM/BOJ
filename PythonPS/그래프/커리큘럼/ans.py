import sys
import copy
input = sys.stdin.readline

n = int(input())
lectures = [[] for i in range(n+1)]
lecDegree = [0]*(n+1)
time = [0]

for i in range(1,n+1):
    llist = list(map(int, input().split()))
    time.append(llist[0])
    for j in range(1, len(llist)-1):
        lectures[llist[j]].append(i)
        lecDegree[i]+=1
        
def topological_sort(time, lectures, lecDegree):
    result = copy.deepcopy(time)
    queue = []

    for i in range(1, n+1):
        if lecDegree[i]==0:
            queue.append(i)
            
    while queue:
        now = queue.pop(0)
        for target in lectures[now]:
            result[target] = max(result[target], result[now]+time[target])
            lecDegree[target]-=1
            if lecDegree[target]==0:
                queue.append(target)
                
    return result
        
        
result = topological_sort(time, lectures, lecDegree)

for i in range(1, n+1):
    print(result[i])