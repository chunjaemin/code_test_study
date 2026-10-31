# 입력 받기: 네트워크 입력을 어떻게 처리할 것인가 
# 문제풀이: 네트워크를 어찌저찌 이었다면 어떻게 네트워크의 개수를 샐 것인가?, 그래프를 다 만들고나서 0~N-1 노드를 방문, bfs를 돌려서 방문표시, 방문안한 노드 다시 방문 반복 
from collections import defaultdict, deque
def solution(n, computers):
    g = defaultdict(list)
    N = len(computers)
    visited = [0] * N
    q = deque()
    
    def bfs(a):
        q.append(a)
        visited[a] = 1 
        while q:
            x = q.popleft()
            for nx in g[x]:
                if visited[nx] == 0:
                    visited[nx] = 1 
                    q.append(nx)
    
    for r in range(N):
        for c in range(N):
            if computers[r][c] == 1:
                g[r].append(c)  
                g[c].append(r)
    
    cnt = 0
    for i in range(N):
        if visited[i] == 0:
            cnt += 1 
            bfs(i)
            
    return cnt