from collections import deque
def solution(board):
    answer = -1
    N = len(board)
    M = len(board[0])
    R = [-1,1,0,0]
    C = [0,0,-1,1]
    bd = [list(row) for row in board]
    visited = [[-1] * M for _ in range(N)]
    sr, sc = 0, 0
    er, ec = 0, 0
    for r in range(N):
        for c in range(M):
            if bd[r][c] == "R":
                sr, sc = r, c 
            if bd[r][c] == "G":
                er, ec = r, c 
    
    q = deque()
    visited[sr][sc] = 0 
    for i in range(4):
        q.append((sr,sc, i))
    while q:
        r, c, d = q.popleft() 
        if r == er and c == ec:
            answer = visited[er][ec]
            break 
        
        for i in range(4):
            nr, nc = r, c 
            while 0<= nr + R[i] < N and 0<= nc + C[i]< M:
                if bd[nr + R[i]][nc + C[i]] == "D":
                    break 
                nr, nc = nr + R[i], nc + C[i]
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1 
                q.append((nr, nc, i))
                
    return answer