from collections import deque 
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    R = [0,0,1,-1]
    C = [1,-1,0,0]
    visited = [[-1] * M for _ in range(N)]
    visited
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q: 
        r, c = q.popleft()
        for i in range(4):
            nr = r + R[i] 
            nc = c + C[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == -1 and maps[nr][nc] == 1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr,nc))
    
    #디버깅용 코드  
    # for row in maps:
    #     print(*(f"{v:3}" for v in row)) 
    # print("")
    # for row in visited:
    #     print(*(f"{v:3}" for v in row)) 
    
    
    ans = visited[N-1][M-1]
                
    return ans