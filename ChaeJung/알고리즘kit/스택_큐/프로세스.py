from collections import deque


def solution(priorities, location):
	answer = 0
	q = deque(enumerate(priorities))
	while q:
		temp = q.popleft()
		if q and temp[1] < max(x[1] for x in q):
			q.append(temp)
		else:
			answer += 1
			if temp[0] == location:
				return answer
