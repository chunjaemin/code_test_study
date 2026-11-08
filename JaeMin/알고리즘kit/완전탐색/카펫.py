# 수학적으로 풀 수 있을 것 같은데 
# 판정 함수 만들고 내부 직사각형 모든 케이스로 판정 때려보기

from itertools import product 
def solution(brown, yellow):
    def check (a, b):
        return brown == (a+2) * (b+2) - a*b
    
    def child(n):
        n_set = set()
        for i in range(1, n+1):
            if n % i == 0: 
                n_set.add(i)
        return n_set
    N = yellow
    ans = [-1,-1]
    
    c_list = child(N)
    comb = product(c_list, repeat = 2)
    
    for x, y in comb: 
        if x * y == N: 
            if check(x,y):
                ans = [x+2, y+2]
    return sorted(ans, reverse = True)