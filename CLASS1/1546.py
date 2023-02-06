loop = int(input())

list = list(map(int, input().split()))

list.sort()
result = 0.0

for i in list:
    result+=i
result = result*100/list[loop-1]/loop
print(result)