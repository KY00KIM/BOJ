loop = int(input())
li = input().split()
min = 0
max = 0

for i in range(loop):
    if i == 0:
        min = int(li[0])
        max = int(li[0])
    else :
        tmp = int(li[i])
        if tmp < min :
            min = tmp
        elif tmp > max :
            max = tmp

print("{} {}".format(min, max))