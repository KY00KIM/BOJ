import sys, heapq
input = sys.stdin.readline

n = int(input())

def findEmpty(start, end):
    tmp = [0,1,2]
    tmp.remove(start)
    tmp.remove(end)
    return tmp[0]

def hanoi(start, end, num):
    if(num<2):
        print(start+1, end+1)
        return 1
    else:
        cnt = hanoi(start, findEmpty(start, end), num-1)
        print(start+1, end+1)
        return cnt + 1



hanoi(0,2, n)
