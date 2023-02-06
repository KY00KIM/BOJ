a, b = input().split()
result = ''

a = int(a)
b = int(b)

if a > b : 
    result = '>'
elif a < b :
    result = '<'
else :
    result = '=='
    
print(result)