from collections import defaultdict

def solution(participant, completion):
    answer = ''
    dict = defaultdict(int)
    for x in participant:
        dict[x] += 1
    for x in completion:
        dict[x] -= 1 
    for k, v in dict.items():
        if v == 1:
            answer = k 
    return answer