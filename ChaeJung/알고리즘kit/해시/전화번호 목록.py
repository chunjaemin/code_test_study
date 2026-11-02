def solution(phone_book):
	phone_set = set(phone_book)
	for i in range(len(phone_book)):
		for j in range(len(phone_book[i])):
			if phone_book[i][:j] in phone_set:
				return False
	return True
