#아니 개어렵네 ㅋㅋㅋㅋ 답지보고 풀었어 이게 level2..?
def solution(phone_book):
    ans = True
    phone_set = set(phone_book)
    for x in phone_set:
        for i in range(1, len(x)):
            if x[:i] in phone_set:
                ans = False
    return ans