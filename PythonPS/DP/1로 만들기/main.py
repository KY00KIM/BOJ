x = int(input())
d = [0]* (x+1)

def findMin(x):
    if x <= 1:
        return 0
    if d[x] != 0:
        return d[x]
    d[x] = 1+ min( findMin(x//5)+(x%5), findMin(x//3)+(x%3), findMin(x-1) )
    return d[x]

print(findMin(x))