input = input().upper()

cnt = 0
result = '?'
s = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for char in s:
    tmp = input.count(char)
    if cnt < tmp :
        cnt = tmp
        result = char
    elif cnt == tmp :
        result = '?'
        
print(result)