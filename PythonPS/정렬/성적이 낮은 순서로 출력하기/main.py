n = int(input())
llist = []
for i in range(n):
    a, b = input().split()
    llist.append((a, int(b)))

llist.sort(key = lambda x : x[1])

for i in llist:
    print(i[0], end=" ")