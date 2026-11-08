from collections import deque


def solution(begin, target, words):
	q = deque()
	visited = [begin]
	q.append((begin, 0))

	def a(begin, words, count):
		for word in words:
			diff = 0
			for i in range(len(begin)):
				if begin[i] != word[i]:
					diff += 1
			if diff == 1 and word not in visited:
				q.append((word, count + 1))
				visited.append(word)

	while q:
		new_begin, count = q.popleft()
		if new_begin == target:
			return count
		a(new_begin, words, count)

	return 0
