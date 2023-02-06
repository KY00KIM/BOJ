import sys, heapq
input = sys.stdin.readline

n = int(input())

def findEmpty(start, end):
    tmp = [0,1,2]
    tmp.remove(start)
    tmp.remove(end)
    return tmp[0]

def hanoi(start, end, num):
    if(num==1):
        print(start+1, end+1, sep = " ")
        return 1
    else:
        cnt = hanoi(start, findEmpty(start, end), num-1)
        print(start+1, end+1, sep = " ")
        cnt += hanoi (findEmpty(start, end),end, num-1)
        return cnt + 1

if(n  > 20):
    print(pow(2, n)-1)
else:
    print(pow(2, n)-1)
    hanoi(0,2, n)
# if(n <= 20):
#     print(course)