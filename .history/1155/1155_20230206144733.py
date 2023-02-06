import sys, heapq
input = sys.stdin.readline

n = int(input())
priority = list(map(int, input().split()))

print(n, "\t", priority)

inf = int(1e9)
