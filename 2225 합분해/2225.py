import sys
import itertools
input = sys.stdin.readline

n, k = map(int, input().split())

'''
{ 0 1 2 ... N } >>> 중복 포함 k개 
합이 N이 나오도록 하는 경우의 수 1e9 로 나눈 나머지

n+1 H k-1 >> n+k-1 C k-1 = 
n / k-1 / (n+k-1)!/(k-1)!n!
n+k-1 C n >> n+k-1, n+k-2, .. , k // n!
a C b = (a+b)! // (a-b)! * (b!)
'''


#res = len(list(itertools.combinations(range(n+k-1), k-1)))
res = 1
for i in range(k-1):
    res *= n+k-1-i
    if i>0:
        res //= (i+1)
    

res = res % int(1e9)
print(res)
