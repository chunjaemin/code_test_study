from collections import deque


def solution(n, edge):
	graph = [[] for _ in range(n + 1)]
	for a, b in edge:
		graph[a].append(b)
		graph[b].append(a)

	visited = [-1] * (n + 1)
	q = deque()
	q.append(1)
	max_num = 1
	visited[1] = max_num

	while q:
		now_q = q.popleft()
		# 3,2
		for i in graph[now_q]:
			if visited[i] == -1:
				q.append(i)
				visited[i] = visited[now_q] + 1

	return visited.count(max(visited))
