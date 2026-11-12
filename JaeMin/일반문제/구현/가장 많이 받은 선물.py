#이문제는 4번인가 풀어봤는데도 한번 풀때 쉽지않네; 오래걸린다 
from collections import defaultdict

def solution(friends, gifts):
    N = len(friends)
    friends_index = {k : i for i, k in enumerate(friends)}

    gift_idx = [0]*N
    next_get = [0]*N
    
    give_list = [[0] * N for _ in range(N)]
    
    for s in gifts:
        a, b = s.split(" ")
        na = friends_index[a]
        nb = friends_index[b]
        give_list[na][nb] += 1 
    
    for i in range(N):
        cnt_give = 0 
        cnt_get = 0 
        for j in range(N):
            cnt_give += give_list[i][j]
            cnt_get += give_list[j][i]
        gift_idx[i] = cnt_give - cnt_get 
    
    for i in range(N):
        for j in range(i+1, N):
            if give_list[i][j] > give_list[j][i]: # i가 더많이 줌 
                next_get[i] += 1
            elif give_list[i][j] < give_list[j][i]: # j가 더많이 줌 
                next_get[j] += 1
            elif give_list[i][j] == give_list[j][i]: # 선물지수 비교 
                if gift_idx[i] > gift_idx[j]:
                    next_get[i] += 1
                elif gift_idx[i] < gift_idx[j]:
                    next_get[j] += 1
    ans = max(next_get)
    return ans
