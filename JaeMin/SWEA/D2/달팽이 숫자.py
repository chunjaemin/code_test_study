
from collections import deque 
N = int(input())

board = [[0] * N for _ in range(N)]
#상우하좌
R = [-1,0,1,0]
C = [0,1,0,-1]

q = deque()
q.append((0,0,1))
board[0][0] = 1
while q:
    r, c, d= q.popleft()

    nr, nc = r + R[d], c + C[d]
    if not (0<= nr < N and 0 <= nc < N) or not (board[nr][nc] == 0):
        d = (d + 1) % 4 
        nr, nc = r + R[d], c + C[d]
        if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] != 0:
            break

    board[nr][nc] = board[r][c] + 1
    q.append((nr,nc,d))

for row in board:
    print(row)