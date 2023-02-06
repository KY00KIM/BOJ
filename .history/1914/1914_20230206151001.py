import sys, heapq
input = sys.stdin.readline

n = int(input())
course = []
def findEmpty(start, end):
    tmp = [0,1,2]
    tmp.remove(start)
    tmp.remove(end)
    return tmp[0]

def hanoi(start, end, num):
    if(num<2):
        course.append(str(start+1) +" "+str(end+1))
        return 1
    else:
        cnt = hanoi(start, findEmpty(start, end), num-1)
        course.append(str(start+1) +" "+str(end+1))
        cnt += hanoi (findEmpty(start, end),end, num-1)
        return cnt + 1


print(hanoi(0,2, n))
print(course)
