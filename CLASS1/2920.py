li = list(map(int, input().split()))

ans = li[0]-li[1]
flag = 0;

for i in range(1, 7):
    if abs(li[i] -li[i+1]) != 1:
        flag = 1

if flag == 1:
    print("mixed")
elif ans == 1:
    print("descending")
else :
    print("ascending")