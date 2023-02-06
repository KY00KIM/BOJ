import re
loop = int(input())

li =[]

for i in range(loop):
    score = 0
    match = re.findall('O+', input())
    for j in range(len(match)):
        score += len(match[j])*(len(match[j])+1)/2
    li.append(int(score))

for i in range(len(li)):
    print(li[i])
