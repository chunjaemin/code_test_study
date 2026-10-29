#priorities배열이 주어지는 순간 실행순서는 고정됨
#숫자가 높으면 무조건 먼저실행, 숫자가 같을 경우 먼저 나온 녀석이 먼저 실행
#생각보다 잔실수 잡기가 많이 어려운 문제인듯, 흠 어떻게 코드를 짜야 실수를 방지할 수 있을지 고민해봐야 할 듯 

from collections import deque 
def solution(priorities, location):
    arr = []
    q = deque()
    for i in range(len(priorities)):
        q.append([priorities[i], i])
    
    done = []
    while q: 
        x, x_loc = q.popleft()
        if q:
            if x >= max(q, key = lambda x : x[0])[0]:
                done.append([x, x_loc])
            else:
                q.append([x,x_loc])
        else:
            done.append([x, x_loc])
    ans = 0
    for i in range(len(done)):
        if done[i][1] == location:
            ans = i+1
    return ans