from collections import deque


def solution(maps):
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	q = deque()
	q.append((0, 0))
	n = len(maps)
	m = len(maps[0])
	dist = [[-1] * m for _ in range(n)]
	dist[0][0] = 1

	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < m:
				if maps[nx][ny] == 1 and dist[nx][ny] == -1:
					dist[nx][ny] = dist[x][y] + 1
					q.append((nx, ny))

	return dist[n - 1][m - 1]
