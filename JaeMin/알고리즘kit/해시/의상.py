from collections import defaultdict 

#해시문제라기보단 수학문제 느낌이네 얘는 수학쓰는거라 level2인가 전화번호 목록에 비하면 훨 쉽네 
def solution(clothes):
    c_dict = defaultdict(int)
    for x_key, x_val in clothes:
        c_dict[x_val] += 1
    
    ans = 1 
    for x in c_dict.values():
        ans *= x + 1 
    return ans - 1
