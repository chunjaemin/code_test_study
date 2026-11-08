# BFS 문제 
from collections import defaultdict, deque
def solution(n, edge):
    g = defaultdict(list)
    q = deque() 
    
    for x, y in edge:
        g[x].append(y) 
        g[y].append(x) 
    
    visited = [0]*(n+1)
    q.append((1,0))
    visited[1] = 1
    ans = 0
    
    while q:
        x, l = q.popleft()
        ans = max(ans, l)
        for nx in g[x]:
            if visited[nx] == 0:
                visited[nx] = l+1 
                q.append((nx, l+1))
                
    max_n = max(visited)
    ans = sum(1 for x in visited if x == max_n)
    return ans