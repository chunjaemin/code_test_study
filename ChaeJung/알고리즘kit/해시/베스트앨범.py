def solution(genres, plays):
	answer = []

	song = {}

	# 장르별로 (고유번호, 재생횟수) 묶기
	for i, genre in enumerate(genres):
		if genre not in song:
			song[genre] = []

		song[genre].append((i, plays[i]))

	# 장르별 총 재생 횟수
	total = {}

	for genre in song:
		total[genre] = sum(play for i, play in song[genre])

	# 총 재생 횟수가 많은 장르 순서
	genre_order = sorted(total, key=total.get, reverse=True)

	# 각 장르에서 최대 2개 선택
	for genre in genre_order:
		songs = sorted(song[genre], key=lambda x: x[1], reverse=True)

		for x in songs[:2]:
			answer.append(x[0])

	return answer
