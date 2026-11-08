def solution(arrows):
	answer = 0

	dx = [0, 1, 1, 1, 0, -1, -1, -1]
	dy = [1, 1, 0, -1, -1, -1, 0, 1]
	# dx = [0, 1, 1, 1, 0, -1, -1, -1]
	# dy = [1, 1, 0, -1, -1, -1, 0, 1]
	edges = set()
	nodes = set()

	now_nodes_x = 0
	now_nodes_y = 0

	nodes.add((0, 0))

	for i in arrows:
		for _ in range(0, 2):
			next_x = now_nodes_x + dx[i]
			next_y = now_nodes_y + dy[i]
			current = (now_nodes_x, now_nodes_y)
			next_node = (next_x, next_y)
			# sorted로 항상 같은 순서로 저장되게 해야함
			# sorted의 반환결과는 리스트임 그래서 튜플로 다시 바꿔줘야함
			edge = tuple(sorted((current, next_node)))

			if next_node in nodes and edge not in edges:
				answer += 1

			edges.add(edge)
			nodes.add(next_node)

			now_nodes_x = next_x
			now_nodes_y = next_y

	return answer
