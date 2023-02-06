import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline


T = int(input())

def insertQ (QM, Qm, Q, data):
    heapq.heappush(QM, -(data))
    heapq.heappush(Qm, data)
    Q[data] += 1
    return

def delMax(QM, Q):
    while len(QM):
        target = -(heapq.heappop(QM))
        if Q[target] != 0:
            Q[target] -= 1
            break
    return
   

def delMin(Qm, Q):
    while len(Qm):
        target = heapq.heappop(Qm)
        if Q[target] != 0:
            Q[target] -= 1
            break
    return 


for i in range(T):
    QM = []
    Qm = []
    Q = defaultdict(int)
    k = int(input())
    
    for _ in range(k):
        op, n = input().split()
        n = int(n)
        if op == 'I':
            insertQ(QM, Qm ,Q, n)
        elif n == 1:
            delMax(QM, Q)
        else: 
            delMin(Qm, Q)
    
    while QM and Q[-QM[0]]==0:
        heapq.heappop(QM)
    while Qm and Q[Qm[0]]==0:
        heapq.heappop(Qm)

    if not QM: print('EMPTY')
    else: print(-QM[0], Qm[0])
   
        