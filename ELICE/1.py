import sys
input = sys.stdin.readline

b = input()
bomb = 0
laser = 0

for i in b:
    if i =="(":
        bomb+=1
    else:
        laser += 1
if bomb == laser:
    print("YES")
else:
    print("NO")