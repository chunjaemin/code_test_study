from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    N = 200 
    board = [[0] * N for _ in range(N)]
    dist = [[-1] * N for _ in range(N)]

    for x1, y1, x2, y2 in rectangle:
        for x in range(x1 * 2, x2 * 2 + 1):
            for y in range(y1 * 2, y2 * 2 + 1):
                board[x][y] = 1

    for x1, y1, x2, y2 in rectangle:
        for x in range(x1 * 2 + 1, x2 * 2):
            for y in range(y1 * 2 + 1, y2 * 2):
                board[x][y] = 0
                
    sx, sy = characterX * 2, characterY * 2
    ex, ey = itemX * 2, itemY * 2
    
    q = deque()
    q.append((sx,sy))
    dist[sx][sy] = 0
    
    X = [0,0,1,-1]
    Y = [1,-1,0,0]
    ans = 0 
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            ans = dist[x][y] // 2 
            break 
        
        for i in range(4):
            nx = x + X[i]
            ny = y + Y[i]
            if 0<= nx < N and 0 <= ny < N:
                if board[nx][ny] == 1 and dist[nx][ny] == -1:   
                    dist[nx][ny] = dist[x][y] + 1 
                    q.append((nx,ny))

    return ans