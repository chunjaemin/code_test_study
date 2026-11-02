from functools import cmp_to_key


def solution(numbers):
	array = []

	for number in numbers:
		array.append(str(number))

	def compare(a, b):
		if a + b > b + a:
			return -1
		elif b + a > a + b:
			return 1
		else:
			return 0

	a = sorted(array, key=cmp_to_key(compare))

	b = "".join(a)

	if b[0] == "0":
		return "0"

	return b
