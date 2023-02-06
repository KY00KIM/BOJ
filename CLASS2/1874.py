
def stackSeq (llist, loop):
    stack=[]
    result=""
    max = 1
    idx = 0

    for idx in range(loop):
        top = -1            
        if llist[idx] >= max:
            for _ in range(max, llist[idx]+1):
                stack.append(max)
                max+=1
                result+="+\n"
            stack.pop()
            result+="-"
        elif llist[idx] < max:
            if (len(stack)==0) | (llist[idx] != stack[top]):
                return "NO"
            stack.pop()
            result+="-"
        if idx != loop-1:
            result+="\n"
    
    return result
            
        


seq=[]
loop = int(input())

for _ in range(loop):
    seq.append(int(input()))
      
print(stackSeq(seq, loop))
  
