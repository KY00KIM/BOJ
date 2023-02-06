a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)
cnt = []

for ch in range(10) :
    cnt.append(result.count(str(ch)))
    
for i in range (10):
    print(cnt[i])