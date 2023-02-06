def priQueue(seq, n, pri):
    result = 0
    
    while len(seq) != 0:
        target = max(seq)
        while target != seq[0]:
            seq.append(seq.pop(0))
        result += 1
        seq.pop(0)
        if target == pri:
            break
    
    
    
    return result



loop = int(input())

llist = []

for _ in range(loop):
    n, pri = input().split()
    n = int(n)
    pri = int(pri)
    seq = input()