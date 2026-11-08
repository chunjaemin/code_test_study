# DFS 인듯? 와 이게 BFS로 풀리는 문제였네 해설봤음
# DFS, BFS 구분 => "현재 상태"만 중요하고 이전에 뭘 골랐는지 몰라도 된다면 BFS로 풀어도 됨 예를 들어 이문제는 현재 특정 단어에 도달했을 때 이전에 어떤 단어에 왔는지 관계없이 무조건 visited True 해주면 되는 구조기 때문에 bfs를 쓸 수 있음 
# zip함수 독특한데 많이 쓰일 것 같으니 외워두기! 
# sum(x != y for x, y in zip(a, b)) 유용할 듯 
from collections import deque 
def solution(begin, target, words):
    
    q = deque()
    N = len(words)
    K = len(begin)
    visited = [0] * N
    ans = 0 
    
    def cnt_check(a, b):
        return sum(x != y for x, y in zip(a, b))
    
    q.append((begin, 0))
    
    while q:
        x, l = q.popleft()
        if x == target:
            ans = l 
            break 
            
        for i in range(N):
            if visited[i] == 0 and cnt_check(x, words[i]) == 1:
                visited[i] = 1
                q.append((words[i], l+1))
            
    return ans