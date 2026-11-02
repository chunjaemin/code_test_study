def solution(nums):
	nums_len = len(nums) // 2
	return min(nums_len, len(set(nums)))
