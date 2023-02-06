loop = int(input())
resarr = []

for i in range(loop):
    rep, string = input().split()
    rep = int(rep)
    result = ""
    for j in range(len(string)) :
        for k in range (rep) : 
            result += string[j]
    resarr.append(result)
    
for i in range(len(resarr)):
    print(resarr[i])