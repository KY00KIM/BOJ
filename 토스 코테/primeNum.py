import math
import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

MAX = 3000
def solution(n, m):
    #n = 2, 3, 4 Num of div 2 = prime / 3 = prime1 * prime2 / 4 = prime1 * prime2 * prime3
    #m 1~3000 (4,5) = 15, (3,3000) = 7억601 Index
    Prime()
    # print(PrimeSet)
    if n == 2:
        result = PrimeSet[m-1]
        print(result)
    elif n == 3:
        result = PrimeSet[m-1]
        print(result*result)
    elif n == 4:
        result = getCombPrime(m, 3)
        print(result)

        
        
isPrime = [True] * MAX
PrimeSet = []
def Prime():
    for i in range(2, int(math.sqrt(MAX))):
        if isPrime[i]:
            for j in range(i * 2, MAX, i):
                isPrime[j] = False
    for i in range(2, len(isPrime)):
        if isPrime[i]:
            PrimeSet.append(i)
    PrimeSet.sort()

def getCombPrime(idx, llen):
    ls = list(dict.fromkeys(list(map(lambda x:x[0]*x[1] , list(combinations_with_replacement(PrimeSet, llen))))))
    print(ls[0], ls[1], ls[2])
    return ls[idx-1]

    


# a < b < c
# a*a 
# a*b ? 
# a*c ? b*b
# n C 2 = (n*n - n) = 6000



def main():
    n, m = map(int, input().split())
    solution(n, m)

if __name__ == "__main__":
	main()