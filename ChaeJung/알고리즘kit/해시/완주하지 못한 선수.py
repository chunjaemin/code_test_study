from collections import Counter


def solution(participant, completion):
	participant_c = Counter(participant)
	completion_c = Counter(completion)
	left = participant_c - completion_c
	return list(left.keys())[0]
