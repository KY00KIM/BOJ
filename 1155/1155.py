import sys, heapq
input = sys.stdin.readline

def str2int(x):
    if x == 'A':
        return 0
    elif x == 'B':
        return 1
    else:
        return 2
def findTmp(x,y):
    tmp = [0,1,2]
    tmp.remove(x)
    tmp.remove(y)
    return tmp[0]
    
n = int(input())
priority = list(map(lambda x: (str2int(x[0]),str2int(x[1])),input().split()))
hanoi = [ [ [0 for k in range(31)] for j in range(3)] for i in range(3)]

# print(priority)
for i in range(6):
    start = priority[i][0]
    dest = priority[i][1]
    if hanoi[start][0][1] == 0 and hanoi[start][1][1] == 0 and hanoi[start][2][1] == 0:
        hanoi[start][dest][1] = 1
    
    
for diskNum in range(2, 31):
    for start in range(3):
        for dest in range(3):
            if start == dest:
                continue
            else:
                if hanoi[start][findTmp(start,dest)][diskNum-1] != 0 and hanoi[findTmp(start,dest)][dest][diskNum-1] != 0:
                    hanoi[start][dest][diskNum] = hanoi[start][findTmp(start,dest)][diskNum-1] + 1 + hanoi[findTmp(start,dest)][dest][diskNum-1]
                elif hanoi[start][dest][diskNum-1] != 0 and hanoi[dest][start][diskNum-1] != 0:
                    hanoi[start][dest][diskNum] = 2 * hanoi[start][dest][diskNum-1] + hanoi[dest][start][diskNum-1] + 2;

res = 0
if hanoi[0][1][n] == 0:
    res = hanoi[0][2][n]
else:
    res = hanoi[0][1][n]
print(res)