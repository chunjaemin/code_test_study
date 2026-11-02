def solution(clothes):
	c = {}
	answer = 0

	for i in range(len(clothes)):
		if clothes[i][1] not in c:
			c[clothes[i][1]] = []
		c[clothes[i][1]].append(clothes[i][0])

	answer = 1

	for category in c:
		answer *= len(c[category]) + 1

	# 아무것도 입지 않는 경우 제외
	return answer - 1


# 의상 종류를 key로, 의상 이름들을 list로 묶어서 딕셔너리 만들기
# 각 의상 종류에서 "하나를 선택하거나 아무것도 선택하지 않는 경우"를 계산
# 각 종류의 (의상 개수 + 1)을 모두 곱하기
# 아무것도 입지 않는 경우 1개를 빼고 반환
