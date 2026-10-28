# 1. 각 작업별 배포일 배열형태로 구하고 
# 2. 큐형태로 첫요소 빼서 자기보다 큰 숫자가 나오기 전까지 pop하면서 카운팅하기 

from collections import deque
def solution(progresses, speeds):
    N = len(progresses)
    q = deque()
    ans = []
    for i in range(N):
        progress = progresses[i]
        day = 0
        while progress < 100:
            progress += speeds[i]
            day += 1 
        q.append(day)
    while q:
        x = q.popleft()
        cnt = 1 
        while q and x >= q[0]:
            q.popleft()
            cnt += 1
        ans.append(cnt)
    return ans