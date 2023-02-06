import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for i in range(T):
    QM = []
    Qm = []
    Q = defaultdict(int)
    k = int(input())
    for _ in range(k):
        op, n = input().split()
        n = int(n)
        if op == 'I':
            #insertQ(QM, Qm ,Q, n)
            heapq.heappush(QM, -n)
            heapq.heappush(Qm, n)
            Q[n] += 1
        elif n == 1:
            #delMax(QM, Q)
            while QM:
                target = -(heapq.heappop(QM))
                if Q[target] != 0:
                    Q[target] -= 1
                    break
        else: 
            #delMin(Qm, Q)
            while Qm:
                target = heapq.heappop(Qm)
                if Q[target] != 0:
                    Q[target] -= 1
                    break
    while QM and Q[-QM[0]]==0:
        heapq.heappop(QM)
    while Qm and Q[Qm[0]]==0:
        heapq.heappop(Qm)

    if not QM: print('EMPTY')
    else: print(-QM[0], Qm[0])
   