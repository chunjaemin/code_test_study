from collections import Counter

def solution(participant, completion):
    answer = ''
    cnt1 = Counter(participant)
    cnt2 = Counter(completion)
    total_cnt = cnt1 - cnt2
    return total_cnt.most_common()[0][0]