n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    a[i], b[i] = b[i], a[i]

ans = 0
for i in a:
    ans+=i
print(ans)
