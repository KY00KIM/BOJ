cnt = 0
max = 0

for i in range(9):
    a = int(input())
    if a > max:
        cnt = i+1
        max = a
        
print(max)
print(cnt)
    