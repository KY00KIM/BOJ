
def BFS (G, N):
    result = [ i for i in range (N+1)]
    
    queue = []
    visited = [0] * (N+1)
    queue.append(1)
    visited[1] = 1
    
    while len(queue) != 0:
        node = queue.pop(0)
        
        for i in G[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                result[i] = node

    return result            
                
        
    




N = int(input())
G = dict()

for _ in range (1,N+1):
    G.setdefault(_, [])

for i in range(N-1):
    n, m = map(int, input().split())
    G[n].append(m)
    G[m].append(n)
    
answer = BFS(G, N)

for i in range(2, N+1):
    print(answer[i])



