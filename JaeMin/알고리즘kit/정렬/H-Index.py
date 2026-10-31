# 이거 진짜 헷갈린다 코드는 짧은데 문제이해를 엉성하게 하면 시간 많이 쓸 것 같은 유형이네 다시한번 풀어봐야할 유형인듯, 직관적으로 풀지말고 정말 맞는 풀이인지 정검하면서 풀도록 하기 

from collections import Counter
def solution(citations):
    N = len(citations)
    ans = 0 
    citations.sort()
    for i in range(N):
        h = N - i
        if h <= citations[i]:
            ans = h 
            break
    return ans