#가장 짧은 길이 일 때 기록하기, 같은 길이는 갱신 X 더 짧을 때만 갱신하기 
import sys
from collections import Counter, defaultdict 
def solution(gems):
    gem_dict = Counter(gems)
    gem_list = list(gem_dict.keys())

    ch_dict = defaultdict(int)
    
    N = len(gems)
    n_gems = len(gem_list)
    l, r = 0, 0 
    ans_l = 0
    ans_r = sys.maxsize
    gems_check = 0 
    #보석 추가하기
    for r in range(N):
        ch_dict[gems[r]] += 1
        if ch_dict[gems[r]] == 1:
            gems_check += 1 
        # while 문으로 왼쪽에 있는 보석 제거하기 
        while l <= r:
            if ch_dict[gems[l]] - 1 > 0:
                ch_dict[gems[l]] -= 1
                l += 1 
            else:
                break 
        
        if gems_check == n_gems:
            if ans_r - ans_l > r - l: 
                ans_r = r
                ans_l = l 
            
    answer = [ans_l+1, ans_r+1]
    return answer