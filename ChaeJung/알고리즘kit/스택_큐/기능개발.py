def solution(progresses, speeds):
	answer = []
	temp = []

	for i in range(len(speeds)):
		days = (100 - progresses[i] + speeds[i] - 1) // speeds[i]
		temp.append(days)

	current = temp[0]
	count = 1

	for i in range(1, len(temp)):
		if temp[i] <= current:
			count += 1
		else:
			answer.append(count)
			count = 1
			current = temp[i]

	answer.append(count)
	return answer
